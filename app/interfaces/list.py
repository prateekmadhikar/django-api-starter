from app.models.list import List as ListModel


class List:

    def __init__(self, list):
        self._list = list
        self._id = list.id
        self._name = list.name
        self._created_at = list.created_at
        self._updated_at = list.updated_at

    def __repr__(self):
        return self._list.__repr__()

    def for_list_id(self, list_id):
