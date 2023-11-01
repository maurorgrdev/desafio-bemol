from flask import request 
from flask_restx import Resource, fields
from flask_restx.utils import default_id
import requests

from domain.models.address import AddressModel
from insfrastructure.schemas.address import AddressSchema

from server.instance import server

address_ns = server.address_ns

address_schema = AddressSchema()
address_list_schema = AddressSchema(many=True)

item = address_ns.model('Address',{
    'uf'          : fields.String(description='Address uf'         ),
    'cep'         : fields.String(description='Address cep'        ),
    'tipo'        : fields.String(description='Address tipo'       ),
    'bairro'      : fields.String(description='Address bairro'     ),
    'numero'      : fields.String(description='Address numero'     ),
    'logradouro'  : fields.String(description='Address logradouro' ),
    'localidade'  : fields.String(description='Address localidade' ),
    'complemento' : fields.String(description='Address complemento'),
    'user_id'     : fields.Integer(description='Address user_id'),
})

ITEM_NOT_FOUND = 'User not found'

class Address(Resource):
    @address_ns.doc('Get an Item')
    def get(self, id):
        address_data = AddressModel.find_by_id(id)
        if address_data:
            return address_schema.dump(address_data), 200

        return {'message': ITEM_NOT_FOUND}, 404

    @address_ns.doc('Update an Item')
    def put(self, id):
        address_data = AddressModel.find_by_id(id)
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

        address_data.save_to_db()

        return address_schema.dump(address_data), 200


    @address_ns.doc('Delete an item')
    def delete(self, id):
        address_data = AddressModel.find_by_id(id)

        if address_data:
            address_data.delete_from_db()
        
        return {'message': 'Registro excluido com sucesso'}, 201

class AddressList(Resource):
    def get(self):
        return address_list_schema.dump(AddressModel.find_all()), 200
    
    @address_ns.expect(item)
    @address_ns.doc('Create an item')
    def post(self):
        address_json = request.get_json()

        address_data = address_schema.load(address_json)

        address_data.save_to_db()

        return {'message' : 'Registro feito com sucesso'}, 201