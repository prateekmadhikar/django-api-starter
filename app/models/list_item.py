from datetime import datetime

from app import db


class ListItem(db.Model):

    __tablename__ = 'list_item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text, default='')
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'))

    def __repr__(self):
        return u"<{class_name}(\
                    id={self.id}, \
                    name={self.name}, \
                    description={self.description}, \
                    created_at={self.created_at}, \
                    updated_at={self.updated_at} \
                    list_id={self.list_id} \
                )>".format(
                    class_name=self.__class__.__name__,
                    self=self
                )
