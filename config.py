import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_fallback_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
