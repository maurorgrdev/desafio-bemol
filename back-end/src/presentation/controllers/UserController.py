from flask import request
from flask_restx import Resource, fields
from flask_restx.utils import default_id

from application.user_service import UserService


from server.instance import server

user_ns = server.user_ns

user_service = UserService()


item = user_ns.model('User', {
    'cpf'              : fields.String(description='User cpf'             ),
    'name'             : fields.String(description='User name'            ),
    'email'            : fields.String(description='User email'           ),
    'password'         : fields.String(description='User password'        ),
    'confirm_email'    : fields.String(description='User confirm email'   ),
    'confirm_password' : fields.String(description='User confirm password'),
    'data_nascimento'  : fields.DateTime(description='User data nascimento'),
})

class User(Resource):
    @user_ns.doc('Get an Item')
    def get(self, id):
        return user_service.find_by_id(id)

    @user_ns.expect(item)
    @user_ns.doc('Update an Item')
    def put(self, id):
        return user_service.update(request, id)
    
    @user_ns.doc('Delete an item')
    def delete(self, id):
        return user_service.delete(id)
class UserList(Resource):
    def get(self):
        return user_service.find_all()
    
    @user_ns.expect(item)
    @user_ns.doc('Create an item')
    def post(self):
        return user_service.store(request)