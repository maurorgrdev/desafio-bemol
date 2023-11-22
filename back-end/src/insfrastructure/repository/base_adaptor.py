class BaseAdaptor(object):

    entity = NotImplementedError

    def find_by_id(self, entity_id):
        raise NotImplementedError

    def find_by_id_or_fail(self, entity_id):
        raise NotImplementedError

    def save_to_db(self, entity):
        raise NotImplementedError