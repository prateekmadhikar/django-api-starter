from app import db
from app.exceptions import InvalidListIDException
from app.models.list import List as ListModel
from app.interfaces.list import List


class ListService:

    def create_list(self, name):
        list = ListModel(name=name)

        db.session.add(list)
        db.session.commit()

        return List(list)

    def get_all_lists(self):
        lists = ListModel.query.all()

        return [List(l) for l in lists]

    def get_list(self, list_id):
        try:
            return List.for_id(list_id)
        except InvalidListIDException:
            return None

    def delete_list(self, list_id):
        list = self.get_list(list_id)

        if list:
            list.delete()
            return True
        return False

    def update_list(self, list_id, name=None):
        list = self.get_list(list_id)

        if list:
            return list.update(name=name)
        return None
