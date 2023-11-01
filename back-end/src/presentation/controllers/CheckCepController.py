from flask import request 
from flask_restx import Resource, fields
from flask_restx.utils import default_id
from server.instance import server
import json as json

check_cep_ns = server.check_cep_ns

import requests

item = check_cep_ns.__class__('CepModelView', {
    'uf'          : fields.String(description='User uf'                 ),
    'cep'         : fields.String(description='User cep'                ),
    'gia'         : fields.String(description='User gia'                ),
    'ddd'         : fields.String(description='User ddd'                ),
    'ibge'        : fields.String(description='User confirm ibge'       ),
    'siafi'       : fields.String(description='User confirm siafi'      ),
    'bairro'      : fields.String(description='User confirm bairro'     ),
    'logradouro'  : fields.String(description='User confirm logradouro' ),
    'localidade'  : fields.String(description='User confirm licalidade' ),
    'complemento' : fields.String(description='User confirm complemento'),
})

class CheckCep:
    @check_cep_ns.expect({'cep' : fields.String})
    @check_cep_ns.doc('Validate an CEP')
    def check_cep():
        cep_json = request.get_json()

        ufs_authorized = ['AM']

        # print(cep_json)
        # return cep_json
        hehe = requests.get(f"https://viacep.com.br/ws/{cep_json['cep']}/json/")

        if hehe.status_code == 400:
            return {'message': 'CEP inválido'}, 401
        address_cep = hehe.json()
        # return  address_cep['uf']
        if address_cep['uf'] in ufs_authorized:
            # cepModelView = CepModelView(
            #     address_cep['uf'], address_cep['cep'], address_cep['gia'], address_cep['ddd'], address_cep['ibge'],
            #     address_cep['siafi'], address_cep['bairro'], address_cep['logradouro'], address_cep['localidade'],  address_cep['complemento']
            # )
            # cepModelView.uf          = address_cep['uf']
            # cepModelView.cep         = address_cep['cep']
            # cepModelView.gia         = address_cep['gia']
            # cepModelView.ddd         = address_cep['ddd']
            # cepModelView.ibge        = address_cep['ibge']
            # cepModelView.siafi       = address_cep['siafi']
            # cepModelView.bairro      = address_cep['bairro']
            # cepModelView.logradouro  = address_cep['logradouro']
            # cepModelView.localidade  = address_cep['localidade']
            # cepModelView.complemento = address_cep['complemento']

            # cepModelView = json.dumps(cepModelView)
            # print(cep_json)
            return {
                'uf'     : address_cep['uf'],
                'cep'    : address_cep['cep'],
                'gia'    : address_cep['gia'],
                'ddd'    : address_cep['ddd'],
                'ibge'   : address_cep['ibge'],
                'siafi'  : address_cep['siafi'],
                'bairro' : address_cep['bairro'],
                'logradouro'  : address_cep['logradouro'],
                'localidade'  : address_cep['localidade'],
                'complemento' : address_cep['complemento'],
            }, 200
        else:
            return {'message': "Válido apenas CEP do Amazonas"}, 401
            

class CepModelView():
    def __init__(self, cep, logradouro, complemento, bairro, localidade, uf, ibge, gia, ddd, siafi):            
        self.uf          = uf
        self.cep         = cep
        self.gia         = gia
        self.ddd         = ddd
        self.ibge        = ibge
        self.siafi       = siafi
        self.bairro      = bairro
        self.logradouro  = logradouro
        self.localidade  = localidade
        self.complemento = complemento

    def json(self):
        return {
            'uf'     : self.uf,
            'cep'    : self.cep,
            'gia'    : self.gia,
            'ddd'    : self.ddd,
            'ibge'   : self.ibge,
            'siafi'  : self.siafi,
            'bairro' : self.bairro,
            'logradouro'  : self.logradouro,
            'localidade'  : self.localidade,
            'complemento' : self.complemento,
        }
            
            
