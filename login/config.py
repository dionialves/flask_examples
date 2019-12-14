import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storege.db')
DEBUG = True
SECRET_KEY = 'KUc35eZCrBSWZD3mNDGl'

SQLALCHEMY_TRACK_MODIFICATIONS = False
FLASK_ENV = 'development'
