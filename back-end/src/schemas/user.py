from flask_sqlalchemy import model
from marshmallow_sqlalchemy import load_instance_mixin, fields
from ma import ma
from models.user import UserModel
from schemas.address import AddressSchema
from marshmallow import Schema, fields, pprint

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        include_relationships = True
    
    addresses = fields.Nested(AddressSchema, many=True)
    # id = fields.Int(dump_only=True)
    # name = fields.Str()
    # cpf = fields.Str()
    # email = fields.Str()
    # password = fields.Str()
    # confirm_email = fields.Str()
    # confirm_password = fields.Str()
    # addresses = fields.List(fields.Nested(AddressSchema()), dump_only=True)