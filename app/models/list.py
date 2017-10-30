from datetime import datetime

from app import db


class List(db.Model):

    __tablename__ = 'list'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())
    list_items = db.relationship('List Item', backref='list', lazy='dynamic')

    def __repr__(self):
        return u"<{class_name}(\
                    id={self.id}, \
                    name={self.name}, \
                    created_at={self.created_at}, \
                    updated_at={self.updated_at} \
                )>".format(
                    class_name=self.__class__.__name__,
                    self=self
                )
