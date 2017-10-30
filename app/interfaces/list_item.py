
class ListItem:

    def __init__(self, list_item):
        self._list_item = list_item
        self._id = list_item.id
        self._name = list_item.name
        self._description = list_item.description
        self._created_at = list_item.created_at
        self._updated_at = list_item.updated_at

    def __repr__(self):
        return self._list_item.__repr__()