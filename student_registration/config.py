import os

# General
DEBUG = True
SECRET_KEY = 'KUc35eZCrBSWZD3mNDGl'

# SQLite3
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storege.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
