''' varous URL routes '''
# pylint: disable = missing-function-docstring, logging-format-interpolation
import logging
from . import APP


@APP.route('/')
def root():
    logging.info('root')
    return 'root'
