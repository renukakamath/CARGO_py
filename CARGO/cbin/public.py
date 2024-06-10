from flask import *
from database import *
public=Blueprint('public',__name__)

@public.route('/',methods=['get','post'])
def home():
	session.clear()
	
	return render_template('home.html')

@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		uname=request.form['uname']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(uname,password)
		res=select(q)
		if res:
			session['lid']=res[0]['login_id']
			if res[0]['user_type']=='admin':
				return redirect(url_for('admin.adminhome'))
			if res[0]['user_type']=='branch':
				q="select branch_id,branch_name from branches where login_id='%s'"%(session['lid'])
				res=select(q)
				session['bname']=res[0]['branch_name']
				session['bid']=res[0]['branch_id']
				return redirect(url_for('branch.branchhome'))
			if res[0]['user_type']=='staff':
				q="select * from staffs where login_id='%s'"%(session['lid'])
				res=select(q)
				print(res)
				session['sid']=res[0]['staff_id']
				session['sname']=res[0]['first_name']+" "+res[0]['last_name']
				return redirect(url_for('staff.staffhome'))
			# if res[0]['user_type']=='dboy':
			# 	q="select * from deliveryboys where username='%s'"%(uname)
			# 	res=select(q)
			# 	print(res)
			# 	session['did']=res[0]['boy_id']
			# 	session['dname']=res[0]['first_name']+" "+res[0]['last_name']
			# 	return redirect(url_for('dboy.dboyhome'))
			# if res[0]['user_type']=='customer':
			# 	q="select * from customers where username='%s'"%(uname)
			# 	res=select(q)
			# 	print(res)
			# 	session['cid']=res[0]['customer_id']
			# 	session['cname']=res[0]['first_name']+" "+res[0]['last_name']
			# 	return redirect(url_for('customer.customerhome'))
		else:
			flash("COMPLETE REGISTRATION BEFORE LOGIN")
	return render_template('login.html')

@public.route('/customerreg',methods=['get','post'])
def customerreg():
	data={}
	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		ph=request.form['phone']
		email=request.form['email']
		lat=request.form['lat']
		lon=request.form['lon']
		uname=request.form['uname']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(uname,password)
		res=select(q)
		if res:
			flash('THIS USER NAME AND PASSWORD ALREADY TAKEN BY ANOTHER USER')
			return redirect(url_for('public.customerreg'))
		else:
			q="insert into login values('%s','%s','customer')"%(uname,password)
			lid=insert(q)
			
			q="insert into customers values(NULL,'%s','%s','%s','%s','%s','%s','%s')"%(uname,fname,lname,ph,email,lat,lon)
			insert(q)
			return redirect(url_for('public.customerreg'))
	return render_template('customerreg.html',data=data)
