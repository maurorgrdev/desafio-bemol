from enum import unique
from db import db

class AddressModel(db.Model):
    __tablename__ = 'addresses'

    id          = db.Column(db.Integer   , primary_key=True)
    uf          = db.Column(db.String(2) , nullable=False)
    cep         = db.Column(db.String(8) , nullable=False)
    tipo        = db.Column(db.String(80), nullable=False)
    bairro      = db.Column(db.String(80), nullable=False)
    numero      = db.Column(db.String(80), nullable=False)
    localidade  = db.Column(db.String(80), nullable=False)
    logradouro  = db.Column(db.String(80), nullable=False)
    complemento = db.Column(db.String(80), nullable=False)
    user_id     = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    def __init__(self, cep, logradouro, bairro, localidade, uf, tipo, numero, complemento, user_id):
        self.cep         = cep
        self.uf          = uf
        self.tipo        = tipo
        self.bairro      = bairro
        self.numero      = numero
        self.logradouro  = logradouro
        self.localidade  = localidade
        self.complemento = complemento
        self.user_id     = user_id

    def __repr__(self) -> str:
        return f'AddressModel(cep={self.cep}, logradouro={self.logradouro}, bairro={self.bairro}, localidade={self.localidade}, uf={self.uf}, tipo={self.tipo}, numero={self.numero}, complemento={self.complemento}, user_id={self.user_id})'
    
    def json(self):
        return {
            'uf'          : self.uf,
            'cep'         : self.cep,
            'tipo'        : self.tipo,
            'bairro'      : self.bairro,
            'numero'      : self.numero,
            'logradouro'  : self.logradouro,
            'localidade'  : self.localidade,
            'complemento' : self.complemento,
            'user_id'     : self.user_id,
        }
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
        
    @classmethod
    def find_by_cep(cls, cep):
        return cls.query.filter_by(cep=cep).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
