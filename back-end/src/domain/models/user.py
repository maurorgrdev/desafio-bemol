from enum import unique
from db import db
from domain.models.address import AddressModel
from marshmallow import fields

class UserModel(db.Model):
    __tablename__ = 'users'

    id               = db.Column(db.Integer, primary_key=True)
    name             = db.Column(db.String(80), nullable=False, unique=True)
    cpf              = db.Column(db.String(14), nullable=False, unique=True)
    email            = db.Column(db.String(60), nullable=False, unique=True)
    password         = db.Column(db.String(60), nullable=False, unique=False)
    confirm_email    = db.Column(db.String(60), nullable=False, unique=False)
    confirm_password = db.Column(db.String(60), nullable=False, unique=False)
    data_nascimento  = db.Column(db.DateTime, nullable=False)
    addresses        = db.relationship(AddressModel, backref='users', cascade="delete", lazy=True)

    def __init__(self, **kwargs):
        super(UserModel, self).__init__(**kwargs)

    def __repr__(self):
        return f'UserModel(name = {self.name}, cpf = {self.cpf}, email = {self.email}, confirm_email = {self.confirm_email}, password = {self.password}, confirm_password = {self.confirm_password}, data_nascimento={self.data_nascimento})'
    
    def json(self):
        return {
            'name'             : self.name,
            'cpf'              : self.cpf,
            'email'            : self.email,
            'confirm_email'    : self.confirm_email,
            'password'         : self.password,
            'confirm_password' : self.confirm_password,
            'data_nascimento'  : self.data_nascimento,
        }    