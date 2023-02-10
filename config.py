from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:

    SECRET_KEY = environ.get('SECRET_KEY')
    UPLOAD_FOLDER = 'static/files'
    TEMPLATES_FOLDER = 'templates'
