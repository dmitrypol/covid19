''' varous URL routes '''
# pylint: disable = bad-continuation
import logging
from flask import request, redirect, url_for
from flask import render_template
from . import APP, CACHE, models, schemas, formatters


@APP.errorhandler(404)
def error_404(exc):
    logging.error(f'{request} {exc}')
    return redirect(url_for('index'))


@APP.route('/', methods=['GET'])
@CACHE.cached(query_string=True)
def index():
    logging.info('index')
    objs = models.Location.query(order_by=models.Location.state)
    if request.args.get('format') == 'json':
        #   https://github.com/marshmallow-code/flask-marshmallow/issues/50
        schema = schemas.Location(many=True, only=('name', 'county', 'state', 'country'))
        return schema.dumps(objs)
    list_objs = list(objs)
    return render_template('index.html', objs=list_objs, heading='United States',
                           chart_data=formatters.format_chart_data(list_objs),
                           last_confirmed=formatters.last_confirmed(list_objs),
                           last_deaths=formatters.last_deaths(list_objs)
                           )


@APP.route('/<string:name>', methods=['GET'])
def show(name):
    logging.info(f'show {name}')
    try:
        obj = models.Location.load(name)
        if request.args.get('format') == 'json':
            return schemas.Location().dumps(obj)
        return render_template('show.html', heading=f'{obj.county} County, {obj.state}, {obj.country}',
                               chart_data=formatters.format_chart_data([obj]),
                               last_confirmed=formatters.last_confirmed([obj]),
                               last_deaths=formatters.last_deaths([obj]),
                               )
    except KeyError:
        #   looking up by state
        objs = models.Location.query(models.Location.state == name)
        if request.args.get('format') == 'json':
            schema = schemas.Location(many=True)
            return schema.dumps(objs)
        list_objs = list(objs)
        return render_template('show.html', heading=f'{name} State',
                               chart_data=formatters.format_chart_data(list_objs),
                               last_confirmed=formatters.last_confirmed(list_objs),
                               last_deaths=formatters.last_deaths(list_objs)
                               )
