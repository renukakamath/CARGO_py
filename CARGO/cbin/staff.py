from flask import *
from database import *
import uuid
staff=Blueprint('staff',__name__)
 

@staff.route('/staffhome',methods=['get','post'])
def staffhome():
	sname=session['sname']
	sid=session['sid']
	print(sname)

	return render_template('staffhome.html',sname=sname)

@staff.route('/staff_cargo_rqst',methods=['get','post'])
def staff_cargo_rqst():
	data={}
	sid=session['sid']
	q="select branch from staffs where staff_id='%s'"%(sid)
	res=select(q)
	brid=res[0]['branch']
	data={}
	q="select * from bookings inner join customers using(customer_id) inner join prices using(price_id) where branch_id='%s'"%(brid)
	res=select(q)
	data['booking']=res
	print(res)
	if 'action' in request.args:

		boid=request.args['id']
		q="select * from bookings inner join prices using(price_id) where booking_id='%s'"%(boid)
		res=select(q)
		data['updater']=res
		print(res)
	if 'action2' in request.args:
		boid=request.args['id']
		q="select * from deliveryboys where branch_id='%s'"%(brid)
		res=select(q)
		data['boy']=res
	if 'update' in request.form:
		kg=request.form['kg']
		l=request.form['h']
		w=request.form['w']
		floc=request.form['floc']
		tloc=request.form['tloc']
		amt=request.form['amt']
		q="update bookings set weight='%s',length='%s',width='%s',from_location='%s',to_location='%s',amount='%s',booking_status='confirm' where booking_id='%s'"%(kg,l,w,floc,tloc,amt,boid)
		print(q)
		lid=insert(q) 
		flash("CONFORMATION SUCESS")
		return redirect(url_for('staff.staff_cargo_rqst'))
	if 'submit' in request.form:
		dboy=request.form['dboy']
		q="update bookings set boy_id='%s',booking_status='assign' where booking_id='%s'"%(dboy,boid)
		update(q)
		return redirect(url_for('staff.staff_cargo_rqst'))
	return render_template('staff_cargo_rqst.html',data=data)
