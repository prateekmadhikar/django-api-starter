from app import db
from app.models.list_item import ListItem as ListItemModel


class ListItemService:

    def __init__(self):
        pass

    def create_list_item(self, list_id, name, description=None):
        pass

    def get_all_list_items_for_list(self, list_id):
        pass

    def get_list_item(self, list_item_id):
        pass

    def delete_list_item(self, list_item_id):
        pass

    def update_list_item(self, list_item_id, name=None, description=None, list_id=None):
        pass
