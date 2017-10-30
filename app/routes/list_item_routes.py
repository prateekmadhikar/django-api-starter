from flask import Blueprint

list_item_blueprint = Blueprint('list_items', __name__, url_prefix='/list_items')
# list_item_service


@list_item_blueprint.route('/', methods=['GET'])
def get_all_list_items():
    pass


@list_item_blueprint.route('/', methods=['POST'])
def create_list_item():
    pass


@list_item_blueprint.route('/{list_item_id}', methods=['GET'])
def get_list_item(list_item_id):
    pass


@list_item_blueprint.route('/{list_item_id}', methods=['PUT'])
def update_list_item(list_item_id):
    pass


@list_item_blueprint.route('/{list_item_id}', methods=['DELETE'])
def delete_list_item(list_item_id):
    pass
