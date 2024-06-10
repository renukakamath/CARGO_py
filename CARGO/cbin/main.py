from flask import *
from public import public
from admin import admin
from branch import branch
from staff import staff
from dboy import dboy
from customer import customer
from api import api


app=Flask(__name__)
app.secret_key="hello"
app.register_blueprint(public)
app.register_blueprint(branch,url_prefix='/branch')
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(staff,url_prefix='/staff')
app.register_blueprint(dboy,url_prefix='/dboy')
app.register_blueprint(customer,url_prefix='/customer')
app.register_blueprint(api,url_prefix='/api')
app.run(debug=True,port=5056,host="0.0.0.0")
