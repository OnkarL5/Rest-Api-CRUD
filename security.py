from werkzeug.security import safe_str_cmp, check_password_hash
from models.user import UserModel

def authenticate(EmailId, Password):
	user = UserModel.find_by_email(EmailId)
	if user and check_password_hash(user.Password, Password):
		return user

def identity(payload):
	user_id = payload['identity']
	return UserModel.find_by_id(user_id)
