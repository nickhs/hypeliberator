class Config(object):
    HOST = "localhost"
    PORT = 8080
    HYPEM_ENDPOINT = "http://api.hypem.com/playlist/loved"
    HYPEM_KEY = "51356937edaa4eeef5a3f6ba7e52f0d7"
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'


class ProductionConfig(Config):
    DEBUG = False
