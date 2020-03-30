''' config settings '''
import os
from logging.config import dictConfig
#import redis, fakeredis
from walrus import Database


APP_NAME = os.environ.get('app_name')
HOME_DIR = os.environ.get('home_dir')
LOGS_DIR = f'{HOME_DIR}logs/'
TMP_DIR = f'{HOME_DIR}tmp/'
APP_ENV = os.environ.get('APP_ENV', 'dev')
SECRET_KEY = 'foobar'
START_DATE = '03-22-2020'   #   date for which there is good data

REDIS_HOST = os.environ.get('REDIS_HOST')

CACHE_DEFAULT_TIMEOUT = 600
CACHE_TYPE = 'redis'
CACHE_REDIS_HOST = REDIS_HOST
CACHE_REDIS_DB = 0

RQ_DASHBOARD_REDIS_HOST = os.environ.get('REDIS_HOST')
RQ_DASHBOARD_REDIS_URL = f'redis://{REDIS_HOST}:6379/1'
RQ_REDIS_URL = f'redis://{REDIS_HOST}:6379/1'

REDLOCK_CONN = [{'host': REDIS_HOST, 'port': 6379, 'db': 2}]
REDIS_JOBSTORE_DB = 2

#REDIS_CLIENT = redis.StrictRedis(host=REDIS_HOST, port=6379, db=3, charset='utf-8', decode_responses=True)
WALRUS_DB = Database(host=REDIS_HOST, port=6379, db=3, decode_responses=True)


if APP_ENV == 'test':
    CACHE_TYPE = 'null'
    #REDIS_CLIENT = fakeredis.FakeStrictRedis(decode_responses=True)
    WALRUS_DB = Database(host=REDIS_HOST, port=6379, db=15, decode_responses=True)


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
