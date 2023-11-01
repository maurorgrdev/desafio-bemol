from flask_sqlalchemy import model
from marshmallow_sqlalchemy import load_instance_mixin, fields
from marshmallow import EXCLUDE
from ma import ma
from domain.models.address import AddressModel

class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AddressModel
        load_instance = True
        include_fk = True
        include_relationships = True
        
    
