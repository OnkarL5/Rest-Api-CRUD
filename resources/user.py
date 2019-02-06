from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.user import UserModel
#changed

class UserRegister(Resource):
	parser = reqparse.RequestParser()

	parser.add_argument('FirstName',
		type=str,
		required=True,
		help="FirstName cannot be blank"
	)

	parser.add_argument('LastName',
		type=str,
		required=True,
		help="LastName cannot be blank"
	)

	
	parser.add_argument('EmailId',
		type=str,
		required=True,
		help="Email cannot be blank"
	)
	
	parser.add_argument('City',
		type=str,
		required=True,
		help="City cannot be blank"
	)

	parser.add_argument('Phone',
		type=str,
		required=True,
		help="phone cannot be blank"
	)

	parser.add_argument('DoB',
		type=str,
		required=True,
		help="Dobl cannot be blank"
	)

	parser.add_argument('UserId',
		type=str,
		required=True,
		help="UserId cannot be blank"
	)

	parser.add_argument('MembershipType',
		type=str,
		required=True,
		help="Email cannot be blank"
	)
	
	parser.add_argument('MembershipSince',
		type=str,
		required=True,
		help="MembershipSince cannot be blank"
	)

	parser.add_argument('MembershipTill',
		type=str,
		required=True,
		help="MembershipTill cannot be blank"
	)

	parser.add_argument('Rank',
		type=str,
		required=True,
		help="Rank cannot be blank"
	)

	parser.add_argument('Role',
		type=str,
		required=True,
		help="Role cannot be blank"
	)

	parser.add_argument('Points',
		type=str,
		required=True,
		help="Email cannot be blank"
	)
	parser.add_argument('Password',
		type=str,
		required=True,
		help="password cannot be blank"
	)

	def post(self):
		data = UserRegister.parser.parse_args()

		if UserModel.find_by_email(data['EmailId']):
			return {"message": "A user with that username already exists"}, 400

		user = UserModel(data['FirstName'], data['LastName'], data['EmailId'], data['City'], data['Phone'], data['DoB'], data['UserId'], data['Password'], data['MembershipType'], data['MembershipSince'], data['MembershipTill'], data['Rank'], data['Role'], data['Points'])
		user.save_to_db()
		return {"message": "User created successfully."}, 201


class User(Resource):
	def get(self,EmailId):
		usa = UserModel.find_by_email(EmailId)
		if usa:
			return usa.json(), 200
		return {'message': 'Email not registered'}, 404
