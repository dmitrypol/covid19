''' varous URL routes '''
import logging
from flask import request, jsonify, render_template
from . import APP, CACHE, services


@APP.route('/', methods=['GET'])
@CACHE.cached()
def index():
    logging.info('index')
    data = services.get_data_index()
    if request.args.get('format') == 'json':
        return jsonify(data)
    return render_template('index.html', data=data)


@APP.route('/show/<string:combined_key>', methods=['GET'])
def show(combined_key):
    data = services.get_data_show(combined_key)
    if request.args.get('format') == 'json':
        return jsonify(data)
    return render_template('show.html', data=data)
