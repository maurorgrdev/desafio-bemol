from ma import ma
from domain.models.user import UserModel
from domain.schemas.address import AddressSchema
from marshmallow import fields, validate, validates, ValidationError, validates_schema
from datetime import date

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        include_relationships = True
    
    addresses = fields.Nested(AddressSchema, many=True)

    name = fields.String(validate=validate.Length(min=1, max=80))
    cpf = fields.String(validate=validate.Length(min=1, max=14))
    email = fields.String(validate=validate.Length(min=1, max=60))
    password = fields.String(validate=validate.Length(min=1, max=60))
    confirm_email = fields.String(validate=validate.Length(min=1, max=60))
    confirm_password = fields.String(validate=validate.Length(min=1, max=60))
    data_limite = fields.String(validate=validate.Length(min=1))

    @validates("data_nascimento")
    def validates_data_nascimento(self, data_nascimento):
        idade = calculateAge(date(data_nascimento.year, data_nascimento.month, data_nascimento.day))

        if idade < 18:
            raise ValidationError("Obrigatório usuário ter mais de 18 anos.")

    @validates("cpf")
    def validates_cpf(self, cpf):
        if UserModel.query.filter(UserModel.cpf == cpf).first():
            raise ValidationError("CPF já cadastrado")
        
    @validates("email")
    def validates_email(self, email):
        if UserModel.query.filter(UserModel.email == email).first():
            raise ValidationError("Email já cadastrado")
        
    @validates_schema
    def validate_object(self, data, **kwargs):
        if data["email"] != data['confirm_email']:
            raise ValidationError("E-mail e Confirmar E-mail devem ser iguais")
        
        if data["password"] != data['confirm_password']:
            raise ValidationError("Senha e Confirmar Senha devem ser iguais")

    
def calculateAge(data_limite): 
    today = date.today() 
    age = today.year - data_limite.year - ((today.month, today.day) < (data_limite.month, data_limite.day)) 

    return age 