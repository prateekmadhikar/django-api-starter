import httplib
import json

from flask import Blueprint, Response, request

from app.services.list_service import ListService

list_blueprint = Blueprint('lists', __name__, url_prefix='/lists')
list_service = ListService()


@list_blueprint.route('/', methods=['GET'])
def get_all_lists():
    lists = list_service.get_all_lists()

    response = {
        'lists': [l.to_json_serializable_dict() for l in lists]
    }

    return Response(response=json.dumps(response),
                    status=httplib.OK,
                    mimetype='application/json')


@list_blueprint.route('/', methods=['POST'])
def create_list():
    req_json = request.json

    list = list_service.create_list(req_json['name'])

    return Response(response=json.dumps(list.to_json_serializable_dict()),
                    status=httplib.CREATED,
                    mimetype='application/json')


@list_blueprint.route('/<int:list_id>', methods=['GET'])
def get_list(list_id):
    list = list_service.get_list(list_id)

    if list:
        return Response(response=json.dumps(list.to_json_serializable_dict()),
                        status=httplib.OK,
                        mimetype='application/json')

    return Response(response=json.dumps({'error': 'invalid list_id'}),
                    status=httplib.NOT_FOUND,
                    mimetype='application/json')


@list_blueprint.route('/<int:list_id>', methods=['PUT'])
def update_list(list_id):
    req_json = request.json

    list = list_service.update_list(list_id,
                                    name=req_json.get('name', None))

    if list:
        return Response(response=json.dumps(list.to_json_serializable_dict()),
                        status=httplib.OK,
                        mimetype='application/json')

    return Response(response=json.dumps({'error': 'invalid list_id'}),
                    status=httplib.NOT_FOUND,
                    mimetype='application/json')


@list_blueprint.route('/<int:list_id>', methods=['DELETE'])
def delete_list(list_id):
    is_deleted = list_service.delete_list(list_id)

    if is_deleted:
        return Response(status=httplib.OK,
                        mimetype='application/json')

    return Response(response=json.dumps({'error': 'invalid list_id'}),
                    status=httplib.NOT_FOUND,
                    mimetype='application/json')
