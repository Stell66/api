from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
#  can be mysql 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)


@app.before_first_request
def create_tables():
	db.create_all()
	# create unless exits already 


# initiate JWT object create a new endpoint /auth when call /auth we send it a username and password  which jwt sends to the authenticate function
jwt = JWT(app, authenticate, identity)
# in memory database

# items = []




api.add_resource(Store,'/store/<string:name>')

api.add_resource(Item,'/item/<string:name>')

api.add_resource(ItemList,'/items')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister,'/register')

if __name__ == '__main__':
	from db import db
	# avoid ciecular import 
	db.init_app(app)
	# avoid circular imports 
	app.run(port=5000, debug=True)




