from insfrastructure.repository.address_repository import AddressRepository
from flask import request, json, Response
from flask_restx import Resource, fields
from domain.schemas.address import AddressSchema

address_repository = AddressRepository()
address_schema = AddressSchema()
address_list_schema = AddressSchema(many=True)

ITEM_NOT_FOUND = 'Address not found'

class AddressService:

    def find_by_id(self, id: int):
        address_data = address_repository.find_by_id(id)

        if address_data:
            address_load = address_schema.dump(address_data)
            return Response(
                response=json.dumps({
                    "data": address_load
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
        address_data = address_repository.find_by_id(id)
        address_json = request.get_json()

        address_data.uf          = address_json['uf'         ]
        address_data.cep         = address_json['cep'        ]
        address_data.tipo        = address_json['tipo'       ]
        address_data.bairro      = address_json['bairro'     ]
        address_data.numero      = address_json['numero'     ]
        address_data.logradouro  = address_json['logradouro' ]
        address_data.localidade  = address_json['localidade' ]
        address_data.complemento = address_json['complemento']
        address_data.user_id     = address_json['user_id']
        
        try:
            result_validation = address_schema.validate(address_json)
            address_repository.save_to_db(address_data)
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
        address_data = address_repository.find_by_id(id)

        if not address_data:
            return Response(
                response=json.dumps({
                    "message": ITEM_NOT_FOUND
                }),
                status=404,
                mimetype="application/json"
            )
        
        address_repository.delete_from_db(address_data),

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
                "data": address_list_schema.dump(address_repository.find_all())
            }),
            status=200,
            mimetype="application/json"
        )

    def store(self, request):
        address_json = request.get_json()

        try:
            result_validation = address_schema.validate(address_json)
            address_data = address_schema.load(address_json)
            address_repository.save_to_db(address_data)
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
    