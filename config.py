
class DefaultConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:passpass@localhost/flask_api?unix_socket=/tmp/mysql.sock'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
