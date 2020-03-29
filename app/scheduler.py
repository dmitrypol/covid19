''' run apscheduler '''
#   https://medium.com/better-programming/introduction-to-apscheduler-86337f3bb4a6
import logging, time
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.blocking import BlockingScheduler
import redlock
#from apscheduler.schedulers.background import BackgroundScheduler
from . import APP, jobs


JOBSTORES = {'default': RedisJobStore(host=APP.config.get('REDIS_HOST'), db=APP.config.get('REDIS_JOBSTORE_DB'))}
SCHED = BlockingScheduler(jobstores=JOBSTORES)
#SCHED = BackgroundScheduler(daemon=True, jobstores=JOBSTORES)

#   https://github.com/SPSCommerce/redlock-py
DLM = redlock.Redlock(APP.config.get('REDLOCK_CONN'))


# @SCHED.scheduled_job('interval', hours=1)
def schedule_jobs():
    try:
        my_lock = DLM.lock('schedule_jobs', 10000)  #   in milliseconds
        if my_lock:
            jobs.import_data.queue()
            logging.info('schedule_jobs')
            time.sleep(1)
            DLM.unlock(my_lock)
    except redlock.MultipleRedlockException as exc:
        logging.error(exc)
SCHED.add_job(schedule_jobs, 'cron', hour='*')
