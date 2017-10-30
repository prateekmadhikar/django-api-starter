import httplib
import json

from flask import Blueprint, Response, request

from app.services.list_item_service import ListItemService
from app.services.list_service import ListService

list_item_blueprint = Blueprint('list_items', __name__, url_prefix='/lists/<int:list_id>/items')

list_service = ListService()
list_item_service = ListItemService()


@list_item_blueprint.route('/', methods=['GET'])
def get_all_list_items(list_id):
    return "hi there, {}".format(list_id)
    # list = list_service.get_list(list_id)

    # if not list:
    #     return Response(response=json.dumps({'error': 'invalid list_id'}),
    #                 status=httplib.NOT_FOUND,
    #                 mimetype='application/json')

    # list_items =


@list_item_blueprint.route('/', methods=['POST'])
def create_list_item(list_id):
    pass


@list_item_blueprint.route('/<int:list_item_id>', methods=['GET'])
def get_list_item(list_id, list_item_id):
    pass


@list_item_blueprint.route('/<int:list_item_id>', methods=['PUT'])
def update_list_item(list_id, list_item_id):
    pass


@list_item_blueprint.route('/<int:list_item_id>', methods=['DELETE'])
def delete_list_item(list_id, list_item_id):
    pass
