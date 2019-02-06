from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_cors import CORS

from security import authenticate, identity
from resources.user import UserRegister, User
from models.user import db

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost/postgres';
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SECRET_KEY'] = 'omai-key'
api = Api(app)
db.init_app(app)

#db = sqlalchemy.create_engine('postgresql+psycopg2://postgres:postgres@localhost/postgres')
#connection  = db.connect()

api.add_resource(UserRegister, '/api/register')
api.add_resource(User, '/api/user/<string:EmailId>')

if __name__ == '__main__':
    app.run()
