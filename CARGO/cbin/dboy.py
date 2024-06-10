from flask import *
from database import *
import uuid
dboy=Blueprint('dboy',__name__)
 

@dboy.route('/dboyhome',methods=['get','post'])
def dboyhome():
	dname=session['dname']
	did=session['did']
	print(dname)
	return render_template('dboyhome.html',dname=dname)

@dboy.route('/dboy_view_assigned_cargos',methods=['get','post'])
def dboy_view_assigned_cargos():
	data={}
	dname=session['dname']
	did=session['did']
	q="select * from bookings inner join customers using(customer_id) inner join prices using(price_id) where boy_id='%s'"%(did)
	res=select(q)
	print(q)
	data['works']=res
	print(res)
	if 'action' in request.args:
		id=request.args['id']
		q="select * from cargo_status where booking_id='%s'"%(id)
		res=select(q)
		if res:
			data['status']=res
			data['id']=id
		else:
			data['status']='pending'
			data['id']=id
		print(data['status'])
	if 'action2' in request.args:
		id=request.args['id']
		q="update bookings set booking_status='delivered' where booking_id='%s'"%(id)
		update(q)
		flash("update as delivered")
		return redirect(url_for('dboy.dboy_view_assigned_cargos'))

	if 'submit' in request.form:
		name=request.form['name']
		q="insert into cargo_status values(NULL,'%s','%s',NOW())"%(id,name)
		insert(q)
		flash("CARGO TRACKING STATUS UPDATED")
		return redirect(url_for('dboy.dboy_view_assigned_cargos'))


	return render_template('dboy_view_assigned_cargos.html',data=data)
