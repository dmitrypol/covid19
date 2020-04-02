''' varous URL routes '''
import logging
from flask import request, redirect, url_for
from flask import render_template
from . import APP, CACHE, models, services, schemas


@APP.errorhandler(404)
def error_404(exc):
    logging.error(f'{request} {exc}')
    return redirect(url_for('index'))


@APP.route('/', methods=['GET'])
@CACHE.cached(query_string=True)
def index():
    logging.info('index')
    data = models.Location.all()
    if request.args.get('format') == 'json':
        #   https://github.com/marshmallow-code/flask-marshmallow/issues/50
        schema = schemas.Location(many=True, only=('name', 'county', 'state', 'country'))
        return schema.dumps(data)
    return render_template('index.html', data=data)


@APP.route('/<string:name>', methods=['GET'])
def show(name):
    logging.info(f'show {name}')
    data = models.Location.load(name)
    chart_data = services.format_chart_data(data)
    if request.args.get('format') == 'json':
        return schemas.Location().dumps(data)
    return render_template('show.html', data=data, chart_data=chart_data)
