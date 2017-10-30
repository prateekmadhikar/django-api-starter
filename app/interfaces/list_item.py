from datetime import datetime

from app import db
from app.exceptions import InvalidListItemIDException
from app.models.list_item import ListItem as ListItemModel
from .base import BaseInterface


class ListItem(BaseInterface):

    FIELDS = (
        'id',
        'name',
        'description',
        'created_at',
        'updated_at',
        'list_id',
    )

    def __init__(self, list_item):
        self._model = list_item

        self._id = list_item.id
        self._name = list_item.name
        self._description = list_item.description
        self._created_at = list_item.created_at
        self._updated_at = list_item.updated_at
        self._list_id = list_item.list_id

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at

    @property
    def list_id(self):
        return self._list_id


    def update(self, name=None, description=None, list_id=None):
        changes_made = False

        if name:
            changes_made = True
            self._model.name = name

        if description:
            changes_made = True
            self._model.description = description

        if list_id:
            changes_made = True
            self._model.list_id = list_id

        if changes_made:
            self._model._updated_at = datetime.now()

            self = cls(self)
            db.session.commit()

        return self

    @classmethod
    def for_id(id):
        list_item = ListItemModel.query.filter_by(id=id).first()

        if list_item:
            return cls(list_item)
        raise InvalidListItemIDException
