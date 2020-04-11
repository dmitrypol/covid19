''' run apscheduler '''
#   https://medium.com/better-programming/introduction-to-apscheduler-86337f3bb4a6
import logging, time
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.blocking import BlockingScheduler
#from apscheduler.schedulers.background import BackgroundScheduler
import redlock
from . import APP, jobs


JOBSTORES = {'default': RedisJobStore(host=APP.config.get('REDIS_HOST'), db=APP.config.get('REDIS_JOBSTORE_DB'))}
SCHED = BlockingScheduler(jobstores=JOBSTORES)
#SCHED = BackgroundScheduler(daemon=True, jobstores=JOBSTORES)
logging.getLogger('apscheduler').setLevel(logging.WARNING)

#   https://github.com/SPSCommerce/redlock-py
DLM = redlock.Redlock(APP.config.get('REDLOCK_CONN'))


# @SCHED.scheduled_job('interval', hours=1)
def import_data():
    try:
        my_lock = DLM.lock('import_data', 10000)  #   in milliseconds
        if my_lock:
            jobs.import_data.queue()
            logging.info('import_data')
            time.sleep(1)
            DLM.unlock(my_lock)
    except redlock.MultipleRedlockException as exc:
        logging.exception(exc)
SCHED.add_job(import_data, 'cron', hour='*')


def refresh_hp():
    try:
        my_lock = DLM.lock('refresh_hp', 10000)  #   in milliseconds
        if my_lock:
            jobs.get_url('http://147.154.10.44')
            jobs.get_url('http://147.154.10.44?format=json')
            logging.info('refresh_hp')
            time.sleep(1)
            DLM.unlock(my_lock)
    except redlock.MultipleRedlockException as exc:
        logging.exception(exc)
SCHED.add_job(refresh_hp, 'interval', seconds=APP.config.get('CACHE_DEFAULT_TIMEOUT'))
