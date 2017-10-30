from flask import Blueprint

from app.services.list_service import ListService

list_blueprint = Blueprint('lists', __name__, url_prefix='/lists')
list_service = ListService()


@list_blueprint.route('/', methods=['GET'])
def get_all_lists():
    lists = list_service.get_all_lists()

    response = {
        'lists': [l.to_json() for l in lists]
    }

    return response


@list_blueprint.route('/', methods=['POST'])
def create_list():

    pass


@list_blueprint.route('/{list_id}', methods=['GET'])
def get_list(list_id):
    pass


@list_blueprint.route('/{list_id}', methods=['PUT'])
def update_list(list_id):
    pass


@list_blueprint.route('/{list_id}', methods=['DELETE'])
def delete_list(list_id):
    pass
