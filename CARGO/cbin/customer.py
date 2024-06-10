from flask import *
from database import *
import uuid
customer=Blueprint('customer',__name__)
 

@customer.route('/customerhome',methods=['get','post'])
def customerhome():
	cname=session['cname']
	cid=session['cid']
	print(cname)
	return render_template('customerhome.html',cname=cname)


@customer.route('/customer_view_cargos',methods=['get','post'])
def customer_view_cargos():
	data={}
	cname=session['cname']
	cid=session['cid']
	q="select * from prices"
	res=select(q)
	print(res)
	data['cargo']=res
	return render_template('customer_view_cargos.html',data=data)

@customer.route('/customer_sendfeedback',methods=['get','post'])
def customer_sendfeedback():
	data={}
	cid=session['cid']
	q="select * from branches"
	res=select(q)
	data['branch']=res
	print(res)
	if 'submit' in request.form:
		fb=request.form['fb']
		bid=request.form['bid']
		q="insert into feedback values(NULL,'%s','%s','%s','pending',NOW())"%(cid,bid,fb)
		res=insert(q)
		return redirect(url_for('customer.customer_sendfeedback'))
	q="select * from feedback inner join branches using(branch_id) where customer_id='%s'"%(cid)	
	res=select(q)
	data['fb']=res
	print(res)
	return render_template('customer_sendfeedback.html',data=data)

@customer.route('/customer_book',methods=['get','post'])
def customer_book():
	pid=request.args['id']
	data={}
	q="select * from branches"
	res=select(q)
	data['branch']=res
	print(res)
	cid=session['cid']
	q="select * from prices where price_id='%s'"%(pid)
	res=select(q)
	data['price']=res
	print(res)
	if 'submit' in request.form:
		kg=request.form['kg']
		l=request.form['len']
		width=request.form['width']
		floc=request.form['floc']
		tloc=request.form['tloc']
		brid=request.form['bid']
		
		q="insert into bookings values(NULL,'%s',NOW(),'%s','%s','%s','%s','%s','%s','pending','pending','pending','%s')"%(cid,brid,kg,l,width,floc,tloc,pid)
		print(q)
		lid=insert(q)
		flash("booked sucessfully")
		return redirect(url_for('customer.customer_book',id=pid))

	return render_template('customer_book.html',data=data)

@customer.route('/customer_review_andrate',methods=['get','post'])
def customer_review_andrate():
	data={}
	cid=session['cid']
	q="select * from branches"
	res=select(q)
	data['branch']=res
	print(res)
	q="select * from review_rating inner join branches using(branch_id) where customer_id='%s'"%(cid)
	res=select(q)
	data['rating']=res
	print(res)
	if 'submit' in request.form:
		bid=request.form['bid']
		rate=request.form['rate']
		review=request.form['review']
		q="select * from review_rating where customer_id='%s' and branch_id='%s'"%(cid,bid)
		res=select(q)
		if res:
			q="update review_rating set rating_point='%s',review_comment='%s',review_date=NOW() where customer_id='%s' and branch_id='%s' "%(rate,review,cid,bid)
			update(q)
			return redirect(url_for('customer.customer_review_andrate'))		
		else:
			print("&&&&&&&&&&&&&&&&&&&&&&&&&")
			q="insert into review_rating values(NULL,'%s','%s','%s','%s',NOW())"%(cid,bid,review,rate)
			res=insert(q)
			return redirect(url_for('customer.customer_review_andrate'))
	# q="select * from feedback inner join branches using(branch_id) where customer_id='%s'"%(cid)	
	# res=select(q)
	# data['fb']=res
	# print(res)
	return render_template('customer_review_andrate.html',data=data)


@customer.route('/customer_view_bookings',methods=['get','post'])
def customer_view_bookings():
	data={}
	cid=session['cid']
	data={}
	cid=session['cid']
	q="select * from bookings inner join branches using(branch_id) where customer_id='%s'"%(cid)
	res=select(q)
	data['bookings']=res
	print(res)
	if 'action' in request.args:
		action=request.args['action']
		boid=request.args['boid']	
		amt=request.args['amt']
		
		q="select * from payment where booking_id='%s'"%(boid)
		res=select(q)
		if res:
			flash("ALREADY PAID")
			return redirect(url_for('customer.customer_track_cargo'))
			
		else:
			data['amt']=amt

	else:
		action=None
	if 'pay' in request.form:
		amt=request.args['amt']

		q="insert into payment values(NULL,'%s','%s',NOW())"%(boid,amt)
		insert(q)
		# q="insert into cargo_status values(NULL,'%s','pending',NOW()"%(boid)
		# insert(q)
		q="update bookings set booking_status='payed' where booking_id='%s'"%(boid)
		update(q)
		return redirect(url_for('customer.customer_track_cargo'))
		flash("PAYMENT SUCESS")


	return render_template('customer_view_bookings.html',data=data)


@customer.route('/customer_track_cargo',methods=['get','post'])
def customer_track_cargo():
	data={}
	cid=session['cid']
	data={}
	cid=session['cid']
	q="select * from bookings inner join branches using(branch_id) inner join payment using(booking_id) where customer_id='%s'"%(cid)
	res=select(q)
	data['bookings']=res
	print(res)
	if 'action' in request.args:
		boid=request.args['boid']
		q="SELECT * FROM `cargo_status` WHERE `booking_id`='%s'"%(boid)
		res=select(q)
		if res:
			data['track']=res
		else:
			data['wait']="wait"

	return render_template('customer_track_cargo.html',data=data)