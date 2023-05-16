import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret'
    DB_HOST = '127.0.0.1'
    DB_PORT = 3306
    DB_USER = 'foobar'
    DB_PASSWD = 'foobar'
    DB_DATABASE = 'foobar'
    ITEMS_PER_PAGE = 10
    JWT_AUTH_URL_RULE = '/api/auth'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    PRODUCTION = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

from datetime import datetime,timedelta
JWT_SECRET_KEY = "alita666666"
JWT_EXPIRATION_DELTA = timedelta(seconds=3600*48)
JWT_VERIFY_CLAIMS = ['signature', 'exp', 'iat']
JWT_REQUIRED_CLAIMS = ['exp', 'iat']
JWT_AUTH_ENDPOINT = 'jwt'
JWT_ALGORITHM = 'HS256'
JWT_LEEWAY = timedelta(seconds=10)
JWT_AUTH_HEADER_PREFIX = 'JWT'
JWT_NOT_BEFORE_DELTA = timedelta(seconds=0)