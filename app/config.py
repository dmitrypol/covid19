''' config settings '''
import os
from logging.config import dictConfig

APP_NAME = os.environ.get('app_name')
HOME_DIR = os.environ.get('home_dir')
LOGS_DIR = f'{HOME_DIR}logs/'
TMP_DIR = f'{HOME_DIR}tmp/'
APP_ENV = os.environ.get('APP_ENV', 'dev')
SECRET_KEY = 'foobar'

if APP_ENV == 'test':
    pass

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '{timestamp:%(asctime)s, level:%(levelname)s, module:%(module)s, lineno:%(lineno)d, %(message)s}',
    }},
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'default',
            'filename': f'{LOGS_DIR}{APP_NAME}-{APP_ENV}.log',
            'when': 'D',
            'interval': 1,
            'backupCount': 7
            }
        },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})
