import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
class Config():
    '''
        Set config variables for the flask app
        Using Environment variables where available.
        Otherwise create the config variable if not done already
    '''


    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    FLASK_ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Ryan will never get access to my CSS'
    SQLALCHEMY_DATABASE_URI = 'postgresql://txtlfhtk:o3WS7ymDnVboZq7wHwj64_yfsH-JgiHS@jelani.db.elephantsql.com/txtlfhtk'
    SQLALCHEMY_TRACK_NOTIFICAITONS = False