# REST api for registering and retrieving user data
python, flask, flask-RESTful, flask_jwt, SQLAlchemy

## User Database
FirstName(String(32))
LastName(String(32))
EmailId(String(64))
City(String(32))
Phone(Integer)
DoB(DateTime)
UserId(String(32))
Password(String(500))
MembershipType(String(16))
MembershipSince(DateTime)
MembershipTill(DateTime)
Rank(Integer)
Role(Integer)
Points(Integer)

## endpoints
to register: /api/register  
to retrieve user data: /api/user/<string: name>  

## HTTP status
200 - ok  
201 - insertion successful  
400 - insertion unsuccessful/bad request  
404 - not found  
