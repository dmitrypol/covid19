''' varous URL routes '''
import logging
from flask import request, jsonify, render_template
from . import APP, services


@APP.route('/', methods=['GET'])
def index():
    logging.info('index')
    data = services.get_data()
    if request.args.get('format') == 'json':
        return jsonify(data)
    return render_template('index.html', data=data)
