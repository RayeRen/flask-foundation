import os
from dotenv import load_dotenv

load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_URI_BASE = 'mysql+pymysql://' + DB_USER + ':' + DB_PASS + '@' + DB_HOST + '/'


class Config(object):
    SECRET_KEY = 'REPLACE_ME'


class ProdConfig(Config):
    ENV = 'prod'
    CACHE_TYPE = 'simple'
    SQLALCHEMY_DATABASE_URI = DB_URI_BASE + "qsy_prod"


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'null'
    ASSETS_DEBUG = True
    SQLALCHEMY_DATABASE_URI = DB_URI_BASE + "qsy_dev"


class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_ECHO = True
    CACHE_TYPE = 'null'
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = DB_URI_BASE + "qsy_test"
