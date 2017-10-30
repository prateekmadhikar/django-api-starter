from app import db


class BaseInterface:

    def __init__(self, model):
        self._model = model

    def __repr__(self):
        return self._model.__repr__()

    def delete(self):
        db.session.delete(self._model)
        db.session.commit()
