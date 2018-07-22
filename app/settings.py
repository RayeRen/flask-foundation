import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env', verbose=True)
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
DB_URI_BASE = 'mysql+mysqlconnector://' + DB_USER + ':' + DB_PASS + '@' + DB_HOST + '/'


class Config(object):
    SECRET_KEY = 'REPLACE_ME'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    ENV = 'prod'
    CACHE_TYPE = 'simple'
    SQLALCHEMY_DATABASE_URI = DB_URI_BASE + DB_NAME + "_prod?charset=utf8mb4"


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'null'
    ASSETS_DEBUG = True
    SQLALCHEMY_DATABASE_URI = DB_URI_BASE + DB_NAME + "_dev?charset=utf8mb4"


class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_ECHO = True
    CACHE_TYPE = 'null'
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = DB_URI_BASE + DB_NAME + "_test?charset=utf8mb4"
