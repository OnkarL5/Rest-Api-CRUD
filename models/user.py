from db import db
from werkzeug.security import generate_password_hash
import datetime
#changed
class BaseModel(db.Model):
	__abstract__ = True
class UserModel(BaseModel):
	__tablename__ = 'User_Info'

	FirstName = db.Column(db.String(32), nullable=False)
	LastName = db.Column(db.String(32),nullable=False)
	EmailId = db.Column(db.String(64), unique=True, nullable=False)
	City = db.Column(db.String(32))
	Phone = db.Column(db.Integer)
	DoB = db.Column(db.DateTime)
	UserId = db.Column(db.String(32),primary_key=True)
	Password = db.Column(db.String(500))
	MembershipType = db.Column(db.String(16))
	MembershipSince = db.Column(db.DateTime)
	MembershipTill = db.Column(db.DateTime)
	Rank = db.Column(db.Integer)
	Role = db.Column(db.Integer)
	Points = db.Column(db.Integer)

	def __init__(self, FirstName, LastName, EmailId, City, Phone, DoB, UserId, Password, MembershipType, MembershipSince, MembershipTill, Rank, Role, Points):
		self.FirstName = FirstName
		self.LastName = LastName
		self.EmailId = EmailId
		self.City = City
		self.Phone = Phone
		self.DoB = DoB
		self.UserId = UserId
		self.Password = generate_password_hash(Password, method = 'sha256')
		self.MembershipType = MembershipType
		self.MembershipSince = MembershipSince
		self.MembershipTill = MembershipTill
		self.Rank = Rank
		self.Role = Role
		self.Points = Points

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def find_by_email(cls, EmailId):
		return cls.query.filter_by(EmailId=EmailId).first()

	@classmethod
	def find_by_id(cls, _id):
		return cls.query.filter_by(id=_id).first()

	def json(self):
		return {'FirstName': self.FirstName, 'LastName': self.LastName, 'EmailId': self.EmailId, 'City': self.City,'Phone': self.Phone, 'DoB': self.DoB.strftime('%d/%m/%Y'), 'UserId': self.UserId, 'MembershipType': self.MembershipType,'MembershipSince': self.MembershipSince.strftime('%d/%m/%Y'), 'MembershipTill': self.MembershipTill.strftime('%d/%m/%Y'), 'Rank': self.Rank, 'Role': self.Role, 'Points': self.Points}
