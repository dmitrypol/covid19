''' varous URL routes '''
import logging
from flask import render_template
from . import APP, CACHE, models, services


@APP.route('/', methods=['GET'])
@CACHE.cached()
def index():
    logging.info('index')
    data = models.Location.all()
    # if request.args.get('format') == 'json':
    #     return jsonify(data)
    return render_template('index.html', data=data)


@APP.route('/show/<string:name>', methods=['GET'])
def show(name):
    logging.info(f'show {name}')
    data = models.Location.load(name)
    chart_data = services.format_chart_data(data)
    # if request.args.get('format') == 'json':
    #     return jsonify(data)
    return render_template('show.html', data=data, chart_data=chart_data)
