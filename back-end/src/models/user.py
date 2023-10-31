from enum import unique
from db import db
from models.address import AddressModel
from marshmallow import fields

class UserModel(db.Model):
    __tablename__ = 'users'

    id               = db.Column(db.Integer, primary_key=True)
    name             = db.Column(db.String(80), nullable=False, unique=True)
    cpf              = db.Column(db.String(11), nullable=False, unique=True)
    email            = db.Column(db.String(80), nullable=False, unique=True)
    password         = db.Column(db.String(12), nullable=False, unique=False)
    confirm_email    = db.Column(db.String(80), nullable=False, unique=False)
    confirm_password = db.Column(db.String(12), nullable=False, unique=False)
    addresses        = db.relationship(AddressModel, backref='users', lazy=True)
    
    
    def __init__(self, name, cpf, email, confirm_email, password, confirm_password):
        self.name = name
        self.cpf = cpf
        self.email = email
        self.confirm_email = confirm_email
        self.password = password
        self.confirm_password = confirm_password

    def __repr__(self):
        return f'UserModel(name = {self.name}, cpf = {self.cpf}, email = {self.email}, confirm_email = {self.confirm_email}, password = {self.password}, confirm_password = {self.confirm_password})'
    
    def json(self):
        return {
            'name'   : self.name,
            'cpf'    : self.cpf,
            'email'  : self.email,
            'confirm_email' : self.confirm_email,
            'password' : self.password,
            'confirm_password' : self.confirm_password,
        }
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def find_by_cpf(cls, cpf):
        return cls.query.filter_by(cpf=cpf).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    