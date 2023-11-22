# from domain.models import user
from insfrastructure.repository.user_repository import UserRepository
from flask import request, json, Response
from flask_restx import Resource, fields
from insfrastructure.schemas.user import UserSchema

user_repository = UserRepository()
user_schema = UserSchema()
user_list_schema = UserSchema(many=True)

ITEM_NOT_FOUND = 'User not found'

class UserService:

    def find_by_id(self, id: int):
        user_data = user_repository.find_by_id(id)

        if user_data:
            user_load = user_schema.dump(user_data)
            return Response(
                response=json.dumps({
                    "data": user_load
                }),
                status=200,
                mimetype="application/json"
            )
        
        return Response(
            response=json.dumps({
                'message': ITEM_NOT_FOUND
            }),
            status=404,
            mimetype="application/json"
        )

    def update(self, request, id: int):
        user_data = user_repository.find_by_id(id)
        user_json = request.get_json()

        user_data.cpf              = user_json['cpf'             ]
        user_data.name             = user_json['name'            ]
        user_data.email            = user_json['email'           ]
        user_data.password         = user_json['password'        ]
        user_data.confirm_email    = user_json['confirm_email'   ]
        user_data.confirm_password = user_json['confirm_password']
        user_data.data_nascimento  = user_json['data_nascimento']
        
        

        try:
            result_validation = user_schema.validate(user_json)
            user_repository.save_to_db(user_data)
        except:
            return Response(
                response=json.dumps({
                    "message": result_validation
                }),
                status=422,
                mimetype="application/json"
            )

        return Response(
            response=json.dumps({
                "message": "Registro atualizado com sucesso"
            }),
            status=200,
            mimetype="application/json"
        )

    def delete(self, id: int):
        user_data = user_repository.find_by_id(id)

        if not user_data:
            return Response(
                response=json.dumps({
                    "message": ITEM_NOT_FOUND
                }),
                status=404,
                mimetype="application/json"
            )
        
        user_repository.delete_from_db(user_data),

        return Response(
            response=json.dumps({
                "message": "Registro feito com sucesso!"
            }),
            status=200,
            mimetype="application/json"
        )

    def find_all(self):
        return Response(
            response=json.dumps({
                "data": user_list_schema.dump(user_repository.find_all())
            }),
            status=200,
            mimetype="application/json"
        )

    def store(self, request):
        user_json = request.get_json()

        try:
            result_validation = user_schema.validate(user_json)
            user_data = user_schema.load(user_json)
            user_repository.save_to_db(user_data)
        except:
            return Response(
                response=json.dumps({
                    "message": result_validation
                }),
                status=422,
                mimetype="application/json"
            )

        return Response(
            response=json.dumps({
                "message": "Registro feito com sucesso"
            }),
            status=201,
            mimetype="application/json"
        )
    