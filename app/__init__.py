''' app initializer '''
# pylint: disable=too-few-public-methods, wrong-import-position, cyclic-import, no-member
import os, logging
from flask import Flask, Blueprint
from flask_assets import Environment, Bundle
from flask_caching import Cache
from flask_marshmallow import Marshmallow
from flask_rq2 import RQ
import rq_dashboard
from rq_dashboard.cli import add_basic_auth
import chartkick


APP = Flask(__name__)
APP.config.from_pyfile('config.py')
MA = Marshmallow(APP)

#   https://github.com/metabolize/rq-dashboard-on-heroku/blob/master/app.py#L10-L16
add_basic_auth(
    blueprint=rq_dashboard.blueprint,
    username=os.environ.get('RQ_DASHBOARD_USERNAME'),
    password=os.environ.get('RQ_DASHBOARD_PASSWORD'),
)
APP.register_blueprint(rq_dashboard.blueprint, url_prefix='/rq')

WALRUS_DB = APP.config.get('WALRUS_DB')
RQ_CLIENT = RQ(APP)
CACHE = Cache(APP)

ASSETS = Environment(APP)
JSB = Bundle('main.js', output='tmp/main.js')
ASSETS.register('js_all', JSB)

CK = Blueprint('ck_page', __name__, static_folder=chartkick.js(), static_url_path='/static')
APP.register_blueprint(CK, url_prefix='/ck')
APP.jinja_env.add_extension("chartkick.ext.charts")


from . import cli, routes
