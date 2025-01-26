from db import session


class BaseModal:
    def __init__(self):
        self.__session = session()
        self._query = self._get_query()

    def _get_query(self):
        return self.__session.query(self.__class__)

    def get(self, id):
        return self._query.filter(self.__class__.id == id).one()

    def get_none(self, id):
        return self._query.filter(self.__class__.id == id).one_or_none()
    
    def get_all(self, filter={}):
        return self._query.filter_by(**filter).all()

    def jsonif(self, model, schema, **kwargs):
        _schema = schema()
        return _schema.dump(model, **kwargs)
