from flask import *
from database import *
import uuid
admin=Blueprint('admin',__name__)
 

@admin.route('/adminhome',methods=['get','post'])
def adminhome():
	return render_template('adminhome.html')



@admin.route('/admin_manage_branches',methods=['get','post'])
def admin_manage_branches():
	data={}
	if 'submit' in request.form:
		bname=request.form['bname']
		lat=request.form['lat']
		lon=request.form['lon']
		ph=request.form['phone']
		email=request.form['email']
		uname=request.form['uname']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(uname,password)
		res=select(q)
		if res:
			flash('THIS USER NAME AND PASSWORD ALREADY TAKEN BY ANOTHER USER')
			return redirect(url_for('admin.admin_manage_branches'))
		else:
			q="insert into login values(null,'%s','%s','branch')"%(uname,password)
			lid=insert(q)
			
			q="insert into branches values(NULL,'%s','%s','%s','%s','%s','%s')"%(lid,bname,lat,lon,ph,email)
			insert(q)
			return redirect(url_for('admin.admin_manage_branches'))
	q="select * from branches"
	res=select(q)
	if res:
		data['branch']=res
		print(res)
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=='delete':
		q="delete from login where login_id='%s'"%(id)
		delete(q)
		q="delete from branches where login_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.admin_manage_branches'))
	if action=='update':
		q="select * from branches where login_id='%s'"%(id)
		data['updater']=select(q)
	if 'update' in request.form:
		bname=request.form['bname']
		lat=request.form['lat']
		lon=request.form['lon']
		ph=request.form['phone']
		email=request.form['email']
		q="update branches set branch_name='%s',latitude='%s',longitude='%s',phone='%s',email='%s' where login_id='%s'"%(bname,lat,lon,ph,email,id)
		update(q)
		return redirect(url_for('admin.admin_manage_branches'))
	return render_template('admin_manage_branches.html',data=data)



@admin.route('/admin_view_staff',methods=['get','post'])
def admin_view_staff():
	data={}
	bid=request.args['bid']
	q="select * from staffs where branch='%s'"%(bid)
	res=select(q)
	if res:
		data['staffs']=res
		print(res)

	return render_template('admin_view_staff.html',data=data)

@admin.route('/admin_view_deliveryboy',methods=['get','post'])
def admin_view_deliveryboy():
	data={}
	bid=request.args['bid']
	q="select * from deliveryboys where branch_id='%s'"%(bid)
	res=select(q)
	if res:
		data['deliveryboys']=res
		print(res)

	return render_template('admin_view_deliveryboy.html',data=data)


@admin.route('/admin_manage_cargo_prices',methods=['get','post'])
def admin_manage_cargo_prices():
	data={}
	if 'submit' in request.form:
		maxkg=request.form['maxkg']
		maxh=request.form['maxh']
		maxw=request.form['maxw']
		maxkm=request.form['maxkm']
		maxp=request.form['maxp']
		
		q="insert into prices values(NULL,'%s','%s','%s','%s','%s')"%(maxkg,maxh,maxw,maxkm,maxp)
		insert(q)
		return redirect(url_for('admin.admin_manage_cargo_prices'))

	q="select * from prices"
	res=select(q)
	if res:
		data['price']=res
		print(res)
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=='delete':
		q="delete from prices where price_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.admin_manage_cargo_prices'))
	if action=='update':
		q="select * from prices where price_id='%s'"%(id)
		data['updater']=select(q)
	if 'update' in request.form:
		maxkg=request.form['maxkg']
		maxh=request.form['maxh']
		maxw=request.form['maxw']
		maxkm=request.form['maxkm']
		maxp=request.form['maxp']
		q="update prices set maximum_weight='%s',maximum_height='%s',maximum_width='%s',maximum_distance='%s',minimum_price='%s' where price_id='%s'"%(maxkg,maxh,maxw,maxkm,maxp,id)
		update(q)
		return redirect(url_for('admin.admin_manage_cargo_prices'))
	return render_template('admin_manage_cargo_prices.html',data=data)


@admin.route('/admin_view_feedback',methods=['get','post'])
def admin_view_feedback():
	data={}
	q="SELECT * FROM feedback INNER JOIN branches using(branch_id) inner join customers using(customer_id)"
	res=select(q)
	data['feedbacks']=res
	print(res)
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
		if action=="update":
			q="select * from feedback inner join customers using(customer_id) where feedback_id='%s' "%(id)
			res=select(q)
			data['updater']=res
	if 'update' in request.form:
		reply=request.form['reply']
		q="update feedback set reply='%s' where feedback_id='%s'"%(reply,id)
		update(q)
		return redirect(url_for('admin.admin_view_feedback'))
	return render_template('admin_view_feedback.html',data=data)


@admin.route('/admin_review_andrate',methods=['get','post'])
def admin_review_andrate():
	data={}
	q="select * from review_rating inner join branches using(branch_id) inner join customers using(customer_id)"
	res=select(q)
	print(res)
	data['rating']=res
	print(res)
	# q="select * from feedback inner join branches using(branch_id) where admin_id='%s'"%(cid)	
	# res=select(q)
	# data['fb']=res
	# print(res)
	return render_template('admin_review_andrate.html',data=data)

# @admin.route('/admin_manage_type',methods=['get','post'])
# def admin_manage_type():
# 	data={}
# 	if 'submit' in request.form:
# 		tname=request.form['tname']
# 		q="select * from type where typename='%s'"%(tname)
# 		res=select(q)
# 		if res:
# 			flash("THIS TYPE TOUR PLAN IS ALREADY ADDED")
# 		else:
# 			q="insert into type values(NULL,'%s')"%(tname)
# 			insert(q)
# 	q="select * from type"
# 	res=select(q)
# 	if res:
# 		data['type']=res
# 		print(res)
# 	if 'action' in request.args:
# 		action=request.args['action']
# 		id=request.args['id']
# 	else:
# 		action=None
# 	if action=='delete':
# 		q="delete from type where type_id='%s'"%(id)
# 		delete(q)
# 		return redirect(url_for('admin.admin_manage_type'))
# 	if action=='update':
# 		q="select * from type where type_id='%s'"%(id)
# 		data['updater']=select(q)
# 	if 'update' in request.form:
# 		uptname=request.form['uptname']
# 		q="update type set typename='%s' where type_id='%s'"%(uptname,id)
# 		update(q)
# 		return redirect(url_for('admin.admin_manage_type'))
# 	return render_template('admin_manage_type.html',data=data)


# @admin.route('/admin_manage_landscape',methods=['get','post'])
# def admin_manage_landscape():
# 	data={}
# 	if 'submit' in request.form:
# 		lname=request.form['lname']
# 		q="select * from landscape where landscape='%s'"%(lname)
# 		res=select(q)
# 		if res:
# 			flash("THIS TYPE LANDSCAPE PLAN IS ALREADY ADDED")
# 		else:
# 			q="insert into landscape values(NULL,'%s')"%(lname)
# 			insert(q)
# 	q="select * from landscape"
# 	res=select(q)
# 	if res:
# 		data['landscape']=res
# 		print(res)
# 	if 'action' in request.args:
# 		action=request.args['action']
# 		id=request.args['id']
# 	else:
# 		action=None
# 	if action=='delete':
# 		q="delete from landscape where landscape_id='%s'"%(id)
# 		delete(q)
# 		return redirect(url_for('admin.admin_manage_landscape'))
# 	if action=='update':
# 		q="select * from landscape where landscape_id='%s'"%(id)
# 		data['updater']=select(q)
# 	if 'update' in request.form:
# 		uplname=request.form['uplname']
# 		q="update landscape set landscape='%s' where landscape_id='%s'"%(uplname,id)
# 		update(q)
# 		return redirect(url_for('admin.admin_manage_landscape'))
# 	return render_template('admin_manage_landscape.html',data=data)



# @admin.route('/admin_manage_district',methods=['get','post'])
# def admin_manage_district():
# 	data={}
# 	if 'submit' in request.form:
# 		name=request.form['name']
# 		q="select * from district where district='%s'"%(name)
# 		res=select(q)
# 		if res:
# 			flash("THIS DISTRICT PLAN IS ALREADY ADDED")
# 		else:
# 			q="insert into district values(NULL,'%s')"%(name)
# 			insert(q)
# 	q="select * from district"
# 	res=select(q)
# 	if res:
# 		data['district']=res
# 		print(res)
	
# 	return render_template('admin_manage_district.html',data=data)


# @admin.route('/admin_manage_places',methods=['get','post'])
# def admin_manage_places():
# 	data={}
# 	q="select * from landscape "
# 	data['landscape']=select(q)
# 	did=request.args['did']
# 	q="select * from type"
# 	data['type']=select(q)
# 	print(did)
# 	data['did']=did
# 	name=request.args['name']
# 	print(name)
# 	data['names']=name
# 	print(data["names"])
# 	if 'submit' in request.form:
# 		pname=request.form['name']
# 		des=request.form['des']
# 		lat=request.form['lat']
# 		lon=request.form['lon']
# 		typ=request.form['type']
# 		landscape=request.form['land']

# 		q="select * from place where placename='%s' and district_id='%s'"%(pname,did)
# 		res=select(q)
# 		if res:
# 			flash("THIS PLACE  IS ALREADY ADDED")
# 		else:
# 			q="insert into place values(NULL,'%s','%s','%s','%s','%s')"%(did,pname,des,lat,lon)
# 			res=insert(q)
# 			q="insert into placedetail values(NULL,'%s','%s','%s')"%(res,landscape,typ)
# 			print(q)
# 			print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
# 			insert(q)
			
# 			return redirect(url_for('admin.admin_manage_places',name=name,did=did))
# 	q="select * from place where district_id='%s'"%(did)
# 	res=select(q)
# 	if res:
# 		data['place']=res
# 		print(res)
# 	if 'action' in request.args:
# 		action=request.args['action']
# 		print(action)
# 		id=request.args['id']
# 	else:
# 		action=None
# 	if action=='delete':
# 		q="delete from place where place_id='%s'"%(id)
# 		delete(q)
# 		return redirect(url_for('admin.admin_manage_places',name=name,did=did))
# 	if action=='update':
# 		q="select * from place where place_id='%s'"%(id)
# 		data['updater']=select(q)
# 	if 'update' in request.form:
# 		upname=request.form['upname']
# 		q="update place set placename='%s' where place_id='%s'"%(upname,id)
# 		update(q)		
# 		return redirect(url_for('admin.admin_manage_places',name=name,did=did))
# 	if action=='images':
# 		print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
# 		q="select * from placeimage where place_id='%s'"%(id)
# 		res=select(q)
# 		print(res)
# 		li=[]
# 		for row in res:
# 			if row['filepath'].split(".")[-1]=='jpg':
# 				li=li+[row]
# 				print("************")
# 				print(li)
# 				data['images']=li

# 		data['img']="image"

# 	if action=='videos':
# 		print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
# 		q="select * from placeimage where place_id='%s'"%(id)
# 		res=select(q)
# 		print(res)
# 		li=[]
# 		for row in res:
# 			if row['filepath'].split(".")[-1]=='mp4':
# 				li=li+[row]
# 				print("************")
# 				print(li)
# 				data['video']=li

# 		data['vid']="video"

# 	if 'imgsubmit' in request.form:
# 		f=request.files['file']
# 		path='static/'+str(uuid.uuid4())+f.filename
# 		f.save(path)
# 		print("#####################################")
# 		print(f.filename)
# 		if f.filename.split(".")[-1]=='jpg':

# 			q="insert into placeimage values(NULL,'%s','%s')"%(id,path)
# 			insert(q)
# 			flash("image added sucessfully")
# 		else:
# 			flash("please choose jpg format file")
# 		return redirect(url_for('admin.admin_manage_places',name=name,did=did))


# 	if 'vidsubmit' in request.form:
# 		f=request.files['file']
# 		path='static/'+str(uuid.uuid4())+f.filename
# 		f.save(path)
# 		if f.filename.split(".")[-1]=="mp4":

# 			q="insert into placeimage values(NULL,'%s','%s')"%(id,path)
# 			insert(q)
# 			flash("video added sucessfully")
# 		else:
# 			flash("please choose mp4 file")
# 		return redirect(url_for('admin.admin_manage_places',name=name,did=did))

# 	return render_template('admin_manage_places.html',data=data,name=name,did=did)


# @admin.route('/admin_view_complaints',methods=['get','post'])
# def admin_view_complaints():
# 	data={}
# 	q="SELECT * FROM user INNER JOIN complaint USING(user_id)"
# 	res=select(q)
# 	data['complaints']=res
# 	if 'action' in request.args:
# 		action=request.args['action']
# 		id=request.args['id']
# 		if action=="update":
# 			q="select * from complaint inner join user using(user_id) where complaint_id='%s' "%(id)
# 			res=select(q)
# 			data['updater']=res
# 	if 'update' in request.form:
# 		reply=request.form['reply']
# 		q="update complaint set reply='%s' where complaint_id='%s'"%(reply,id)
# 		update(q)
# 		return redirect(url_for('admin.admin_view_complaints'))
# 	return render_template('admin_view_complaints.html',data=data)


# @admin.route('admin_viewbooks',methods=['get','post'])
# def admin_viewbooks():
# 	data={}
# 	q="select * from items inner join students using(student_id)"
# 	res=select(q)
# 	data['items']=res
# 	return render_template('admin_viewbooks.html',data=data)

# @admin.route('admin_viewexchangehistory',methods=['get','post'])
# def admin_viewexchangehistory():
# 	data={}
# 	q="SELECT * FROM `exchanges` INNER JOIN items USING (`item_id`) INNER JOIN `students` ON (students.`student_id`=`items`.`student_id`)"
# 	data['exchange']=select(q)
# 	return render_template('admin_viewexchangehistory.html',data=data)


# @admin.route('admin_viewpurchase',methods=['get','post'])
# def admin_viewpurchase():
# 	data={}
# 	q="SELECT * FROM purchase INNER JOIN items ON(purchase.`item_id`=`items`.`item_id`) INNER JOIN `students` ON `items`.`student_id`=`students`.`student_id` order by(items.item)"
# 	res=select(q)
# 	data['purchase']=res
# 	return render_template('admin_viewpurchase.html',data=data)