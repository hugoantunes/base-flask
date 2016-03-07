# encoding: utf-8
import os

from flask import Flask
from flask.ext.mongoengine import MongoEngine
os.environ["WERKZEUG_DEBUG_PIN"] = "off"

DEBUG = os.getenv('DEBUG', True)
PORT = int(os.getenv('PORT', '8000'))

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': os.getenv('MONGODB_DATABASE', 'baseflask'),
    'host': os.getenv('MONGODB_HOST', 'mongodb://localhost/baseflask')
}
db = MongoEngine(app)


def register_blueprints(app):
    from home.views import home
    app.register_blueprint(home)

register_blueprints(app)
app.debug = DEBUG
app.secret_key = "4Q\xbf\xee\xde\xe1\xcd\x86(a{\xd6%9\xab97\xafn?t\xde\xf6#"
