
from .base_adaptor import BaseAdaptor

from exception.entity_not_found import EntityNotFoundException
from exception.unexpected_entity import UnexpectedEntityException

from session import get_session

class SqlAlchemyAdaptor(BaseAdaptor):
    entity = NotImplementedError

    def __init__(self):
        self.session = get_session()

    def find_by_id(self, entity_id):
        return self.session.query(self.entity).get(entity_id)

    def find_by_id_or_fail(self, entity_id):
        entity = self.find_by_id(entity_id)

        if not entity:
            raise EntityNotFoundException(
                '{} with id {} was not found.'.format(
                    self.entity.__name__,
                    entity_id
                )
            )

        return entity

    def find_all(self):
        return self.session.query(self.entity).all()
    
    def save_to_db(self, entity):
        if not isinstance(entity, self.entity):
            raise UnexpectedEntityException(
                '{} is not a {}'.format(
                    entity.__class__.__name__,
                    self.entity.__name__
                )
            )
        
        self.session.add(entity)
        self.session.commit()

    def delete_from_db(self, entity):
        self.session.delete(entity)
        self.session.commit()