class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1234@localhost:3306/project?charset=utf8"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1234@localhost:3306/project?charset=utf8"

db = {
    'user' : 'root',
    'paassword' : '1234',
    'host'     : '127.0.0.1',
    'port'     : '3306',
    'database' : 'project'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8" 