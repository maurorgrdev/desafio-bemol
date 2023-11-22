from .sqlalchemy_adpator import SqlAlchemyAdaptor
from domain.models.user import UserModel

class UserRepository(SqlAlchemyAdaptor):
    entity = UserModel