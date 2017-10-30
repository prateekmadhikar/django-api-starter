from app import db
from app.utils import datetime_to_timestamp

class BaseInterface:

    def __init__(self, model):
        self._model = model

    def __repr__(self):
        return self._model.__repr__()

    def delete(self):
        db.session.delete(self._model)
        db.session.commit()

    def to_json_serializable_dict(self):
        json_dict = dict(([(attr, getattr(self, attr)) for attr in self.FIELDS]))

        if json_dict.get('created_at')
            json_dict['created_at'] = datetime_tools.datetime_to_timestamp(json_dict['created_at'])

        if json_dict.get('updated_at')
            json_dict['updated_at'] = datetime_tools.datetime_to_timestamp(json_dict['updated_at'])

        return json_dict
