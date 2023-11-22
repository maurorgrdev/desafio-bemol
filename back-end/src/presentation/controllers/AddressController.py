from flask import request 
from flask_restx import Resource, fields
from flask_restx.utils import default_id
from application.address_service import AddressService

from server.instance import server

address_ns = server.address_ns

address_service = AddressService()

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

class Address(Resource):
    @address_ns.doc('Get an Item')
    def get(self, id):
        return address_service.find_by_id(id)

    @address_ns.expect(item)
    @address_ns.doc('Update an Item')
    def put(self, id):
        return address_service.update(request, id)

    @address_ns.doc('Delete an item')
    def delete(self, id):
        return address_service.delete(id)

class AddressList(Resource):
    def get(self):
        return address_service.find_all()

    @address_ns.expect(item)
    @address_ns.doc('Create an item')
    def post(self):
        return address_service.store(request)