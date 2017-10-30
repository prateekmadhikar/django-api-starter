from app import db
from app.models.list_item import ListItem as ListItemModel
from app.interfaces.list_item import ListItem


class ListItemService:

    def create_list_item(self, list_id, name, description=None):
        list_item = ListItemModel(name=name,
                                  description=description if description else '',
                                  list_id=list_id)
        return ListItem(list_item)

    def get_all_list_items_for_list(self, list_id):
        list_items = ListItemModel.query.filter_by(list_id=list_id).all()

        return [ListItem(li) for li in list_items]

    def get_list_item(self, list_item_id):
        return ListItem.for_id(list_item_id)

    def delete_list_item(self, list_item_id):
        list_item = self.get_list_item(list_item_id)
        list_item.delete()

    def update_list_item(self, list_item_id, name=None, description=None, list_id=None):
        list_item = self.get_list_item(list_item_id)

        return list_item.update(name=name, description=description, list_id=list_id)

