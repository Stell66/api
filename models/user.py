import sqlite3
from db import db

# a helper not what api can interact with 
#   a model is our internal representatoin of an entity whereas resource is an external rep of entity 
#  api client websites or mobile app interact with resources 

# make the class extend db model
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        # self.id = _id
        self.username = username
        self.password = password
        # self.some = 'hi'


        # id is a python keyword
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "SELECT * FROM users WHERE username=?"
        # result = cursor.execute(query,(username,))
        # row = result.fetchone()
        # if row:
        #     # user = cls(row[0],row[1],row[2])
        #     user = cls(*row)
        # else:
        #     user = None
        # connection.close()
        # return user
        return cls.query.filter_by(username=username).first()


    @classmethod
    def find_by_id(cls, id):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "SELECT * FROM users WHERE id=?"
        # result = cursor.execute(query,(_id,))
        # row = result.fetchone()
        # if row:
        #     # user = cls(row[0],row[1],row[2])
        #     user = cls(*row)
        # else:
        #     user = None
        # connection.close()
        # return user
        # avoid id it is a builtin python argument
        return cls.query.filter_by(id=id).first()

        # this is an api : aome eyebrow raising moments  not a rest api 

