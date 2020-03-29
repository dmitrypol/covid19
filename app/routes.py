''' varous URL routes '''
import logging
from flask import request, jsonify, render_template
from . import APP

REDIS_CLIENT = APP.config.get('REDIS_CLIENT')


@APP.route('/', methods=['GET'])
def index():
    logging.info('index')
    if request.args.get('format') == 'json':
        keys = REDIS_CLIENT.keys('*')
        output = []
        for key in keys:
            output.append(REDIS_CLIENT.hgetall(key))
        return jsonify(output)
    return render_template('index.html')
