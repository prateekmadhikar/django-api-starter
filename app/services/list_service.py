from app import db
from app.models.list import List as ListModel
from app.interfaces.list import List

class ListService:

    def create_list(self, name):
        list = ListModel(name=name)
        list = List(list)

        return list

    def get_all_lists(self):
        lists = ListModel.query.all()

        return [List(l) for l in lists]

    def get_list(self, list_id):
        return List.for_list_id(list_id)

    def delete_list(self, list_id):
        list = self.get_list(list_id)
        list.delete()

    def update_list(self, list_id, name=None):
        list = self.get_list(list_id)
        list.update(name=name)

        return list
