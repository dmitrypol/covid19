''' http job '''
# pylint: disable = missing-function-docstring, multiple-imports, duplicate-code
import logging
from . import RQ_CLIENT


@RQ_CLIENT.job()
def import_data():
    logging.info('import_data')
