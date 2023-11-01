from flask_sqlalchemy import model
from marshmallow_sqlalchemy import load_instance_mixin, fields
from ma import ma
from domain.models.user import UserModel
from insfrastructure.schemas.address import AddressSchema
from marshmallow import Schema, fields, pprint

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        include_relationships = True
    
    addresses = fields.Nested(AddressSchema, many=True)