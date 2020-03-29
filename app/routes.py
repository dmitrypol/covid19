''' varous URL routes '''
# pylint: disable = missing-function-docstring, logging-format-interpolation
import logging
from flask import request, jsonify, render_template
from . import APP


@APP.route('/', methods=['GET'])
def index():
    logging.info('index')
    if request.args.get('format') == 'json':
        return jsonify({})
    return render_template('index.html')
