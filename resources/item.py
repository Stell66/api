# import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel



# every resource has to be a class

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
            type=float,
            required=True,
            help="This field cannot be left blank!"
    )
        # data = parser.parse_args()
    parser.add_argument('store_id',
            type=int,
            required=True,
            help="Every item needs a store id."
    )





    @jwt_required()
    def get(self, name):
        # for item in items:
        #   if item['name'] == name:
        # item = next(filter(lambda x: x['name'] == name,items), None)
        # return {'item': item}, 200 if item else 404
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

   

    def post(self, name):
        # if next(filter(lambda x: x['name'] == name,items), None):
        #   # 400 bad request
        #   return {'message': "An item with name '{}' already exists".format(name)}, 400 
        # data = Item.parser.parse_args()
        # # data = request.get_json()
        # item = {'name' : name, 'price' : data['price']}
        # items.append(item)
        # return item, 201
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists".format(name)}, 400
            # 400: something wrong with the request :user's fault
        data = Item.parser.parse_args()
        # item = {'name' : name, 'price' : data['price']}
        item = ItemModel(name,data['price'], data['store_id'])

        try:
            # ItemModel.insert(item)
            # item.insert()
            item.save_to_db()
        except:
            return {'message':'An error occured'}, 500
        # 500 : internal server error : server's fault
        return item.json(), 201
        
   

    def delete(self, name):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "DELETE FROM items WHERE name=?"
        # cursor.execute(query,(name,))
        # connection.commit()
        # connection.close()
        # # global items
        # # items = list(filter(lambda x: x['name'] != name, items))
        # return {'message': 'Item deleted'}
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'Item deleted'}



    def put(self,name):
        
        data = Item.parser.parse_args()
        # data = request.get_json()
        # item = next(filter(lambda x: x['name'] == name,items), None)
        item = ItemModel.find_by_name(name)
        # updated_item = {'name': name,'price': data['price']}
        # updated_item = ItemModel(name,data['price'])

        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])

            # item = {'name': name, 'price': data['price']}
            # items.append(item)
            # try:
            #     # ItemModel.insert(updated_item)
            #     updated_item.insert()
            # except:
            #     return {'message':'An error occurred'}, 500         
        else: 
            item.price = data['price']
            # try:
            #     # ItemModel.update(updated_item)
            #     updated_item.update()
            # except:
            #     return {'message':'An error occurred'}, 500
        item.save_to_db()
        return item.json()    
        # return updated_item.json()


   





class ItemList(Resource):
    def get(self):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "SELECT * FROM items"
        # result = cursor.execute(query)
        # items = []
        # for row in result:
        #     items.append({'name': row[0],'price': row[1]})

        # # connection.commit()
        # # not saving anything here
        # connection.close()
        # return {'items': items}
        return {'items': [item.json() for item in ItemModel.query.all()]}                                                                                                                                                                                           
        # return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}

