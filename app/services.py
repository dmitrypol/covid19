''' services '''
from datetime import datetime, timedelta
from . import APP


def get_import_dates_list():
    output = []
    start_date = datetime.strptime(APP.config.get('START_DATE'), '%m-%d-%Y')
    end_date = datetime.today()
    delta = end_date - start_date
    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        output.append(day.strftime('%m-%d-%Y'))
    return output
