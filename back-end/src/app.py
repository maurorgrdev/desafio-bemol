from presentation.controllers.UserController import User, UserList
from presentation.controllers.AddressController import Address, AddressList

from flask import jsonify

from ma import ma
from db import db

from router import Router

from flask_cors import CORS

from server.instance import server

api = server.api
app = server.app

@app.before_request
def create_tables():
    # db.drop_all()
    db.create_all()

api.add_resource(User, '/users/<int:id>')
api.add_resource(UserList, '/users')

api.add_resource(Address, '/addresses/<int:id>')
api.add_resource(AddressList, '/addresses')

Router.run(app)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()

