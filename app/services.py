''' services '''
from datetime import datetime, timedelta
from . import APP, REDIS_CLIENT


#@CACHE.cached(key_prefix='get_data_index')
def get_data_index():
    keys = REDIS_CLIENT.keys('*')
    output = []
    for key in keys:
        tmp = REDIS_CLIENT.hgetall(key)
        tmp['combined_key'] = key
        output.append(tmp)
    return output


def get_data_show(combined_key):
    return REDIS_CLIENT.hgetall(combined_key)


def get_import_dates_list():
    output = []
    start_date = datetime.strptime(APP.config.get('START_DATE'), '%m-%d-%Y')
    end_date = datetime.today()
    delta = end_date - start_date
    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        output.append(day.strftime('%m-%d-%Y'))
    return output
