from flask import *
from database import *
import demjson
import uuid

api=Blueprint('api',__name__)

@api.route('/login')
def login():
	data={}
	username=request.args['username']
	password=request.args['password']
	q="select * from login where username='%s' and password='%s'"%(username,password)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return demjson.encode(data)



@api.route('/userregister')
def userregister():
	data={}
	fname=request.args['fname']
	lname=request.args['lname']
	email=request.args['email']
	phone=request.args['phone']
	latitude=request.args['latitude']
	longitude=request.args['longitude']
	username=request.args['username']
	password=request.args['password']
	q="select * from login where username='%s'"%(username)
	res=select(q)
	if res:
		data['status']="duplicate"
	else:
		q="insert into login values(null,'%s','%s','user')"%(username,password)
		id=insert(q)
		q="insert into customers values(null,'%s','%s','%s','%s','%s','%s','%s')"%(id,fname,lname,phone,email,latitude,longitude)
		insert(q)
		data['status']="success"
	return demjson.encode(data)





@api.route('/usermanagecomplaints')
def usermanagecomplaints():
	data={}
	lid=request.args['lid']
	complaint=request.args['complaint']
	bid=request.args['bid']
	q="insert into feedback values(null,(select customer_id from customers where login_id='%s'),'%s','%s','pending',curdate())"%(lid,bid,complaint)
	insert(q)
	data['status']="success"
	data['method']="usermanagecomplaints"
	return demjson.encode(data)


@api.route('/userviewcomplaints')
def userviewcomplaints():
	data={}
	lid=request.args['lid']
	bid=request.args['bid']
	q="select * from feedback inner join branches using(branch_id) where customer_id=(select customer_id from customers where login_id='%s') and branch_id='%s'"%(lid,bid)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="userviewcomplaints"
	return demjson.encode(data)


@api.route('/userviewbranch')
def userviewbranch():
	data={}
	q="select * from branches"
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="userviewbranch"
	return demjson.encode(data)





@api.route('/customerviewrating')
def customerviewrating():
	data={}
	lid=request.args['lid']
	q="select * from review_rating where  customer_id=(select customer_id from customers where login_id='%s')" %(lid)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res[0]['rating_point']
		data['review']=res[0]['review_comment']
	else:
		data['status']="failed"
	data['method']='customerviewrating'
	return demjson.encode(data)

@api.route('/customerrating')
def customerrating():
	data={}
	rate=request.args['rate']
	lid=request.args['lid']
	bid=request.args['bid']
	comment=request.args['comment']
	q="select * from review_rating where  customer_id=(select customer_id from customers where login_id='%s') and branch_id='%s'" %(lid,bid)
	res=select(q)
	if res:
		q="update review_rating set rating_point='%s',review_comment='%s' where  customer_id=(select customer_id from customers where login_id='%s') and branch_id='%s'" %(rate,comment,lid,bid)
		update(q)
	else:
		q="insert into review_rating values(null,(select customer_id from customers where login_id='%s'),'%s','%s','%s',curdate())" %(lid,bid,comment,rate)
		insert(q)
	data['status']="success"
	data['method']='customerrating'
	return demjson.encode(data)

@api.route('/userviewbranchss')
def userviewbranchss():
	data={}
	q="select * from branches"
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']='userviewbranchss'
	return demjson.encode(data)








@api.route('/deliveryboyvieworderdispatched')
def deliveryboyvieworderdispatched():
	data={}
	lid=request.args['lid']
	q="select * from bookings inner join customers using(customer_id) inner join prices using(price_id) where boy_id=(select boy_id from deliveryboys where login_id='%s') and booking_status='assign'"%(lid)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="deliveryboyvieworderdispatched"
	return demjson.encode(data)

@api.route('/deliveryboyvieworderpickup')
def deliveryboyvieworderpickup():
	data={}
	lid=request.args['lid']
	q="select * from bookings inner join customers using(customer_id) inner join prices using(price_id) where boy_id=(select boy_id from deliveryboys where login_id='%s') and booking_status='pickup'"%(lid)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="deliveryboyvieworderpickup"
	return demjson.encode(data)


@api.route('/deliveryboyupdatestatustopickup')
def deliveryboyupdatestatustopickup():
	data={}
	oid=request.args['oid']
	q="update `bookings` set booking_status='pickup' where booking_id='%s'"%(oid)
	update(q)
	data['status']="success"
	data['method']="deliveryboyupdatestatustopickup"
	return demjson.encode(data)


@api.route('/deliveryboyupdatestatustodeliverd')
def deliveryboyupdatestatustodeliverd():
	data={}
	oid=request.args['oid']
	q="update `bookings` set booking_status='delivered' where booking_id='%s'"%(oid)
	update(q)
	data['status']="success"
	data['method']="deliveryboyupdatestatustodeliverd"
	return demjson.encode(data)



@api.route('/updatepasslocation',methods=['get','post'])
def updatepasslocation():
	data={}

	latti=request.args['latti']
	longi=request.args['longi']
	logid=request.args['logid']
	
	q="update `deliveryboys` set `latitude`='%s',`longitude`='%s' where `login_id`='%s'"%(latti,longi,logid)
	id=update(q)
	if id>0:
		data['status'] = 'success'
	else:
		data['status'] = 'failed'
	data['method'] = 'updatepasslocation'
	return demjson.encode(data)





@api.route('/userviewcargoservices')
def userviewcargoservices():
	data={}
	lati=request.args['lati']
	longi=request.args['longi']
	
	q="SELECT *,(3959 * ACOS ( COS ( RADIANS('%s') ) * COS( RADIANS( latitude) ) * COS( RADIANS( longitude ) - RADIANS('%s') ) + SIN ( RADIANS('%s') ) * SIN( RADIANS( latitude ) ))) AS user_distance FROM branches HAVING user_distance <40 ORDER BY user_distance ASC " %(lati,longi,lati)
	print(q)
	res=select(q)
	print(res)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return  demjson.encode(data)



@api.route('/usercheckprices')
def usercheckprices():
	data={}
	q="SELECT * FROM `prices`"
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return demjson.encode(data)



@api.route('/userviewrating')
def userviewrating():
	data={}
	lid=request.args['lid']
	bid=request.args['bid']
	q="select * from review_rating where  customer_id=(select customer_id from customers where login_id='%s') and branch_id='%s'" %(lid,bid)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res[0]['rating_point']
		data['review']=res[0]['review_comment']
	else:
		data['status']="failed"
	return demjson.encode(data)



@api.route('/userbookacargo')
def userbookacargo():
	data={}
	lid=request.args['lid']
	bid=request.args['bid']
	pid=request.args['pid']
	weight=request.args['weight']
	length=request.args['length']
	width=request.args['width']
	fromlo=request.args['fromlo']
	toloc=request.args['toloc']
	q="select * from prices where maximum_weight>='%s'and maximum_height>='%s'and maximum_width>='%s' and price_id='%s' "%(weight,length,width,pid)
	res=select(q)
	if res:
		q="insert into bookings values(null,(select customer_id from customers where login_id='%s'),curdate(),'%s','%s','%s','%s','%s','%s','%s','pending','0','%s')"%(lid,bid,weight,length,width,fromlo,toloc,res[0]['minimum_price'],pid)
		insert(q)
		data['status']="success"
	else:
		data['status']="nd"
	return demjson.encode(data)






@api.route('/userviewbookedcargo')
def userviewbookedcargo():
	data={}
	lid=request.args['lid']
	bid=request.args['bid']
	q="SELECT * FROM `bookings` where customer_id=(select customer_id from customers where login_id='%s') and branch_id='%s'"%(lid,bid)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return demjson.encode(data)


@api.route('/usermakepayment')
def usermakepayment():
	data={}
	oid=request.args['oid']
	amount=request.args['amount']
	q="insert into payment values(null,'%s','%s',curdate())"%(oid,amount)
	insert(q)
	q="update `bookings` set booking_status='paid' where booking_id='%s'"%(oid)
	update(q)
	data['status']="success"
	return demjson.encode(data)


@api.route('/userviewdeliveryboys')
def userviewdeliveryboys():
	data={}
	did=request.args['did']
	q="SELECT * FROM `deliveryboys` WHERE boy_id='%s'"%(did)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return demjson.encode(data)
