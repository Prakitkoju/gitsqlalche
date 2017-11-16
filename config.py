import os
basedir = os.path.abspath(os.path.dirname(__file__))

# export DATABASE_URL="postgresql://postgres:postgres@localhost:5000/dbtest"

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.getenv['DATABASE_URL', 'postgresql://postgres:postgres@localhost:5000/dbtest']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True