from .sqlalchemy_adpator import SqlAlchemyAdaptor
from domain.models.address import AddressModel

class AddressRepository(SqlAlchemyAdaptor):
    entity = AddressModel
