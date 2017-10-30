from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import DefaultConfig
from .routes.list_routes import list_blueprint
from .routes.list_item_routes import list_item_blueprint


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DefaultConfig)

    db.init_app(app)
    migrate = Migrate(app, db)

    from models.list_item import ListItem
    from models.list import List

    app.register_blueprint(list_blueprint)
    app.register_blueprint(list_item_blueprint)


    @app.route('/', methods=['GET'])
    def hello_world():
        return 'Hello World', 200

    return app
