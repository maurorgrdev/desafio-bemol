from flask_sqlalchemy import model
from marshmallow_sqlalchemy import load_instance_mixin, fields
from marshmallow import EXCLUDE
from ma import ma
from domain.models.address import AddressModel
from marshmallow import fields, validate, validates, ValidationError, validates_schema

class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AddressModel
        load_instance = True
        include_fk = True
        include_relationships = True
        
    @validates("uf")
    def validates_uf(self, uf):
        ufs_authorized = ['AM']

        if not uf in ufs_authorized:
            raise ValidationError("CEP precisa ser do estado do Amazonas.")
