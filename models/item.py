#  resource : map endpoints get/post verb called by api directly 

#  models only used with our code don't pollute resource with these methods 

# import sqlite3
from db import db 

#  as an internal rep also needs to contain properties of an item


#  method within a class should be seperated by a new line classed should be seperated by two 
class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')
    # cannot delete corresponding store

    def __init__(self, name, price, store_id):

        self.name = name
        self.price = price
        self.store_id = store_id


    def json(self):
        return {'name':self.name, 'price': self.price}


# should still be a class method 
#  cls: reference to the class 
    @classmethod
    def find_by_name(cls, name):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "SELECT * FROM items WHERE name=?"
        # result = cursor.execute(query,(name,))
        # row = result.fetchone()
        # connection.close()
        # if row:
        #     # return {'item':{'name': row[0],'price': row[1]}}
        #     # item = new ItemModel(row[0],row[1])
        #     return cls(*row)
           #  argument unpacking 
        # return an object instead of an dict
        return cls.query.filter_by(name=name).first()
        # limit 1


    
    def save_to_db(self):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor() 
        # query = "INSERT INTO items VALUES (?,?)"
        # cursor.execute(query,(self.name,self.price))
        # connection.commit()
        # connection.close()
        db.session.add(self)
        db.session.commit()
        # both update and insert 

    
    # def update(self):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()
    #     query = "UPDATE items SET price=? WHERE name=?"
    #     cursor.execute(query,(self.price,self.name))
    #     connection.commit()
    #     connection.close()
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()



