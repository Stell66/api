from werkzeug.security import safe_str_cmp
from models.user import UserModel


# users = [
# 	{
# 		'id':1,
# 		'username': 'Bob',
# 		'password': 'asdf'
# 	}
# ]


# Users = [
# 	User(1,'Bob','asdf')
# ]


# username_mapping = {'Bob':{
# 	'id': 1,
# 	'username': 'Bob',
# 	'password': 'asdf'
# 	}
# }

# # set comprehension
# username_mapping = {u.username: u for u in Users}

# userid_mapping = {u.id: u for u in Users}


# userid_mapping = {1:{
# 	'id': 1,
# 	'username': 'Bob',
# 	'password': 'asdf'
# 	}
# }

# without any iteration 

def authenticate(username, password):
	# user = username_mapping.get(username, None)
	user = UserModel.find_by_username(username)
	if user and safe_str_cmp(user.password, password):
		return user 

def identity(payload):
	user_id = payload['identity']
	# return userid_mapping.get(user_id, None)
	return UserModel.find_by_id(user_id)

	




