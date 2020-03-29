''' app initializer  '''
# pylint: disable=too-few-public-methods, wrong-import-position, cyclic-import
import os, logging
from flask import Flask
from flask_rq2 import RQ
import rq_dashboard

APP = Flask(__name__)
APP.config.from_pyfile('config.py')
APP.register_blueprint(rq_dashboard.blueprint, url_prefix='/rq')
RQ_CLIENT = RQ(APP)
REDIS_CLIENT = APP.config.get('REDIS_CLIENT')

from . import cli, routes
