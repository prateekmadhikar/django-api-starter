from datetime import datetime

from app import db
from app.exceptions import InvalidListIDException
from app.models.list import List as ListModel
from .base import BaseInterface


class List(BaseInterface):

    FIELDS = (
        'id',
        'name',
        'created_at',
        'updated_at'
    )

    def __init__(self, list):
        self._model = list

        self._id = list.id
        self._name = list.name
        self._created_at = list.created_at
        self._updated_at = list.updated_at

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at

    def update(self, name=None):
        changes_made = False

        if name:
            changes_made = True
            self._model.name = name

        if changes_made:
            self._model.updated_at = datetime.now()
            self = List(self._model)
            db.session.commit()

        return self

    @classmethod
    def for_id(cls, id):
        list = ListModel.query.filter_by(id=id).first()

        if list:
            return cls(list)
        raise InvalidListIDException
