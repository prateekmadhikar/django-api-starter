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
    list = list_service.get_list(list_id)

    if not list:
        return Response(response=json.dumps({'error': 'invalid list_id'}),
                        status=httplib.NOT_FOUND,
                        mimetype='application/json')

    list_items = list_item_service.get_all_list_items_for_list(list)

    response = {
        'list_items': [l_i.to_json_serializable_dict() for l_i in list_items]
    }

    return Response(response=json.dumps(response),
                    status=httplib.OK,
                    mimetype='application/json')


@list_item_blueprint.route('/', methods=['POST'])
def create_list_item(list_id):
    req_json = request.json

    list = list_service.get_list(list_id)

    if not list:
        return Response(response=json.dumps({'error': 'invalid list_id'}),
                        status=httplib.NOT_FOUND,
                        mimetype='application/json')

    list_item = list_item_service.create_list_item(list,
                                                   req_json['name'],
                                                   description=req_json['description'])

    return Response(response=json.dumps(list_item.to_json_serializable_dict()),
                    status=httplib.CREATED,
                    mimetype='application/json')


@list_item_blueprint.route('/<int:list_item_id>', methods=['GET'])
def get_list_item(list_id, list_item_id):
    list = list_service.get_list(list_id)

    if not list:
        return Response(response=json.dumps({'error': 'invalid list_id'}),
                        status=httplib.NOT_FOUND,
                        mimetype='application/json')

    list_item = list_item_service.get_list_item(list_item_id)

    if not list_item:
        return Response(response=json.dumps({'error': 'invalid list_item_id'}),
                        status=httplib.NOT_FOUND,
                        mimetype='application/json')

    return Response(response=json.dumps(list_item.to_json_serializable_dict()),
                    status=httplib.CREATED,
                    mimetype='application/json')


@list_item_blueprint.route('/<int:list_item_id>', methods=['PUT'])
def update_list_item(list_id, list_item_id):
    req_json = request.json

    list = list_service.get_list(list_id)

    if not list:
        return Response(response=json.dumps({'error': 'invalid list_id'}),
                        status=httplib.NOT_FOUND,
                        mimetype='application/json')

    list_item = list_item_service.update_list_item(list_item_id,
                                                   name=req_json.get('name', None),
                                                   description=req_json.get('description', None))

    if not list_item:
        return Response(response=json.dumps({'error': 'invalid list_item_id'}),
                        status=httplib.NOT_FOUND,
                        mimetype='application/json')

    return Response(response=json.dumps(list_item.to_json_serializable_dict()),
                    status=httplib.OK,
                    mimetype='application/json')


@list_item_blueprint.route('/<int:list_item_id>', methods=['DELETE'])
def delete_list_item(list_id, list_item_id):
    list = list_service.get_list(list_id)

    if not list:
        return Response(response=json.dumps({'error': 'invalid list_id'}),
                        status=httplib.NOT_FOUND,
                        mimetype='application/json')

    is_deleted = list_item_service.delete_list_item(list_item_id)

    if not is_deleted:
        return Response(response=json.dumps({'error': 'invalid list_id'}),
                        status=httplib.NOT_FOUND,
                        mimetype='application/json')

    return Response(status=httplib.OK,
                    mimetype='application/json')
