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


def format_chart_data(data):
    confirmed = []
    for item in data.confirmed.items():
        confirmed.append(list(item))
    deaths = []
    for item in data.deaths.items():
        deaths.append(list(item))
    recovered = []
    for item in data.recovered.items():
        recovered.append(list(item))
    active = []
    for item in data.active.items():
        active.append(list(item))
    return {'confirmed cases':row_date_diff(confirmed), 'number of deaths':row_date_diff(deaths),\
        'recovered cases':row_date_diff(recovered), 'active cases':row_date_diff(active)}


def row_date_diff(row):
    #   [['03-22-2020', '100'], ['03-23-2020', '110'], ['03-24-2020', '130'], ['03-25-2020', '160'], ['03-26-2020', '200']]
    len_row = len(row)
    for index, current in enumerate(row[::-1]):
        if index < len_row - 1:
            prev = row[len_row - index - 2]
            diff = int(current[1]) - int(prev[1])
            row[len_row - index - 1][1] = str(diff)
    return row
