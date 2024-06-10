from database import *
import uuid
from flask import *
branch=Blueprint('branch',__name__)
 

@branch.route('/branchhome',methods=['get','post'])
def branchhome():
	bname=session['bname']
	bid=session['bid']
	print(bname,bid)
	return render_template('branchhome.html',bname=bname)


@branch.route('/branch_manage_staffs',methods=['get','post'])
def branch_manage_staffs():
	data={}
	bname=session['bname']
	bid=session['bid']
	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		ph=request.form['phone']
		email=request.form['email']
		uname=request.form['uname']
		password=request.form['password']
		q="select * from login where username='%s'"%(uname)
		res=select(q)
		if res:
			flash('THIS USER NAME AND PASSWORD ALREADY TAKEN BY ANOTHER USER')
			return redirect(url_for('branch.branch_manage_staffs'))
		else:
			q="insert into login values(null,'%s','%s','staff')"%(uname,password)
			lid=insert(q)
			
			q="insert into staffs values(NULL,'%s','%s','%s','%s','%s','%s')"%(lid,fname,lname,bid,ph,email)
			insert(q)
			return redirect(url_for('branch.branch_manage_staffs'))
	q="select * from staffs where branch='%s'"%(bid)
	res=select(q)
	if res:
		data['staffs']=res
		print(res)
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=='delete':
		q="delete from login where login_id='%s'"%(id)
		delete(q)
		q="delete from staffs where login_id='%s'"%(id)
		delete(q)
		return redirect(url_for('branch.branch_manage_staffs'))
	if action=='update':
		q="select * from staffs where login_id='%s'"%(id)
		data['updater']=select(q)
	if 'update' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		ph=request.form['phone']
		email=request.form['email']
		q="update staffs set first_name='%s',last_name='%s',phone='%s',email='%s' where login_id='%s'"%(fname,lname,ph,email,id)
		update(q)
		return redirect(url_for('branch.branch_manage_staffs'))
	return render_template('branch_manage_staffs.html',data=data)

@branch.route('/branch_manage_deliveryboy',methods=['get','post'])
def branch_manage_deliveryboy():
	data={}
	bid=session['bid']
	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		ph=request.form['phone']
		email=request.form['email']
		uname=request.form['uname']
		password=request.form['password']
		q="select * from login where username='%s'"%(uname)
		res=select(q)
		if res:
			flash('THIS USER NAME AND PASSWORD ALREADY TAKEN BY ANOTHER USER')
			return redirect(url_for('branch.branch_manage_deliveryboy'))
		else:
			q="insert into login values(null,'%s','%s','dboy')"%(uname,password)
			lid=insert(q)
			
			q="insert into deliveryboys values(NULL,'%s','%s','%s','%s','%s','%s','','')"%(lid,fname,lname,bid,ph,email)
			insert(q)
			return redirect(url_for('branch.branch_manage_deliveryboy'))
	q="select * from deliveryboys where branch_id='%s'"%(bid)
	res=select(q)
	if res:
		data['deliveryboys']=res
		print(res)
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=='delete':
		q="delete from login where login_id='%s'"%(id)
		delete(q)
		q="delete from deliveryboys where login_id='%s'"%(id)
		delete(q)
		return redirect(url_for('branch.branch_manage_deliveryboy'))
	if action=='update':
		q="select * from deliveryboys where login_id='%s'"%(id)
		data['updater']=select(q)
	if 'update' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		ph=request.form['phone']
		email=request.form['email']
		q="update deliveryboys set first_name='%s',last_name='%s',phone='%s',email='%s' where login_id='%s'"%(fname,lname,ph,email,id)
		update(q)
		return redirect(url_for('branch.branch_manage_deliveryboy'))
	return render_template('branch_manage_deliveryboy.html',data=data)


@branch.route('branch_reg_cus',methods=['get','post'])
def branch_reg_cus():
	data={}
	q="select * from customers"
	res=select(q)
	data['customers']=res
	return render_template('branch_reg_cus.html',data=data)

@branch.route('/branch_view_bookings',methods=['get','post'])
def branch_view_bookings():
	data={}
	bid=session['bid']
	data={}
	q="select * from bookings inner join customers using(customer_id) where branch_id='%s'"%(bid)
	res=select(q)
	data['booking']=res
	print(res)
	# print(res)
	# cid=session['cid']
	# q="select * from prices where price_id='%s'"%(pid)
	# res=select(q)
	# data['price']=res
	# print(res)
	# if 'submit' in request.form:
	# 	kg=request.form['kg']
	# 	l=request.form['len']
	# 	width=request.form['width']
	# 	floc=request.form['floc']
	# 	tloc=request.form['tloc']
	# 	brid=request.form['bid']
	# 	q="select * from bookings"
	# 	res=select(q)
	# 	if res:
	# 		s="B__"
	# 		prebid=res[0]['booking_id'].split("__")
	# 		print(prebid)
	# 		bid=int(prebid[1])+1
	# 		bid="B__"+str(bid)
	# 		print(bid)
	# 	else:
	# 		bid="B__1"
	# 	q="insert into bookings values('%s','%s',NOW(),'%s','%s','%s','%s','%s','%s','pending','pending','pending')"%(bid,cid,brid,kg,l,width,floc,tloc)
	# 	print(q)
	# 	lid=insert(q)
	# 	flash("booked sucessfully")
	# 	return redirect(url_for('branch.branch_view_bookings',id=pid))

	return render_template('branch_view_bookings.html',data=data)