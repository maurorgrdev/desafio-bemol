from .sqlalchemy_adpator import SqlAlchemyAdaptor
from domain.models.user import UserModel

class UserRepository(SqlAlchemyAdaptor):
    entity = UserModel

    def find_by_id_teste(self, id):
        return  self.session.query(self.entity).filter_by(id=id).first()
    