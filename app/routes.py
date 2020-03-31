''' varous URL routes '''
import logging
from flask import render_template
from . import APP, CACHE, models


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

    confirmed = []
    for item in data.confirmed.items():
        confirmed.append(list(item))
    deaths = []
    for item in data.deaths.items():
        deaths.append(list(item))
    recovered = []
    for item in data.recovered.items():
        recovered.append(list(item))
    active = []
    for item in data.active.items():
        active.append(list(item))
    chart_data = [
        {'name': 'confirmed', 'data': confirmed},
        {'name': 'deaths', 'data': deaths},
        {'name': 'recovered', 'data': recovered},
        {'name': 'active', 'data': active},
        ]

    # if request.args.get('format') == 'json':
    #     return jsonify(data)
    return render_template('show.html', data=data, chart_data=chart_data)
