from flask import request, json, Response
from flask_restx import Resource, fields
from flask_restx.utils import default_id

from models.user import UserModel
from schemas.user import UserSchema

from server.instance import server

user_ns = server.user_ns

user_schema = UserSchema()
user_list_schema = UserSchema(many=True)

item = user_ns.model('User', {
    'cpf'              : fields.String(description='User cpf'             ),
    'name'             : fields.String(description='User name'            ),
    'email'            : fields.String(description='User email'           ),
    'password'         : fields.String(description='User password'        ),
    'confirm_email'    : fields.String(description='User confirm email'   ),
    'confirm_password' : fields.String(description='User confirm password'),
    'data_nascimento'  : fields.DateTime(description='User data nascimento'),
})

ITEM_NOT_FOUND = 'User not found'

class User(Resource):
    @user_ns.doc('Get an Item')
    def get(self, id):
        user_data = UserModel.find_by_id(id)
        if user_data:
            return user_schema.dump(user_data), 200
        
        return {'message': ITEM_NOT_FOUND}, 404

    @user_ns.expect(item)
    @user_ns.doc('Update an Item')
    def put(self, id):
        user_data = UserModel.find_by_id(id)
        user_json = request.get_json()

        user_data.cpf              = user_json['cpf'             ]
        user_data.name             = user_json['name'            ]
        user_data.email            = user_json['email'           ]
        user_data.password         = user_json['password'        ]
        user_data.confirm_email    = user_json['confirm_email'   ]
        user_data.confirm_password = user_json['confirm_password']
        user_data.data_nascimento  = user_json['data_nascimento']

        return user_schema.dump(user_data), 200
    
    @user_ns.doc('Delete an item')
    def delete(self, id):
        user_data = UserModel.find_by_id(id)

        if user_data:
            user_data.delete_from_db()
            return '', 204
        
        return {'message', ITEM_NOT_FOUND}, 404

class UserList(Resource):
    def get(self):
        return user_list_schema.dump(UserModel.find_all()), 200
    
    @user_ns.expect(item)
    @user_ns.doc('Create an item')
    def post(self):
        user_json = request.get_json()
        user_data = user_schema.load(user_json)

        check_cpf = UserModel.find_by_cpf(user_data.cpf)
        if check_cpf:
            return Response(
                response=json.dumps({
                    "message": "CPF já cadastrado"
                }),
                status=401,
                mimetype="application/json"
            )
        
        check_email = UserModel.find_by_email(user_data.email)
        if check_email:
            return Response(
                response=json.dumps({
                    "message": "E-mail já cadastrado"
                }),
                status=401,
                mimetype="application/json"
            )
        
        check_nome = UserModel.find_by_name(user_data.name)
        if check_nome:
            return Response(
                response=json.dumps({
                    "message": "Nome Completo já cadastrado"
                }),
                status=401,
                mimetype="application/json"
            )

        user_data.save_to_db()

        return Response(
            response=json.dumps({
                "message": "Registro feito com sucesso"
            }),
            status=201,
            mimetype="application/json"
        )

        