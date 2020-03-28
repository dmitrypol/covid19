''' app initializer  '''
# pylint: disable=too-few-public-methods, wrong-import-position, cyclic-import
import os, logging
from flask import Flask

APP = Flask(__name__)
APP.config.from_pyfile('config.py')

from . import cli, routes
