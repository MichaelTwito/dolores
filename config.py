import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SUPER_ADMIN_USERNAME = os.environ['SUPER_ADMIN_USERNAME']
    GRPC_PREDICTOR_MANAGER_NODE = os.environ['GRPC_PREDICTOR_MANAGER_NODE']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    DEBUG = False
    TESTING = True
    CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SUPER_ADMIN_USERNAME = os.environ['SUPER_ADMIN_USERNAME']
    # GRPC_PREDICTOR_MANAGER_NODE = os.environ['GRPC_PREDICTOR_MANAGER_NODE']