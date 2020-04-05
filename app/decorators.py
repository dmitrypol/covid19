''' decorators for models '''


def last_confirmed(obj):
    key = obj.confirmed.keys()[-1]
    return obj.confirmed[key]


def last_deaths(obj):
    key = obj.deaths.keys()[-1]
    return obj.deaths[key]


def format_chart_data(obj):
    confirmed = []
    for item in sorted(obj.confirmed.items()):
        confirmed.append(list(item))
    deaths = []
    for item in sorted(obj.deaths.items()):
        deaths.append(list(item))
    return {
        'confirmed':_row_date_diff(confirmed),
        'deaths':_row_date_diff(deaths),
        }


def _row_date_diff(row):
    #   [['03-22-2020', '100'], ['03-23-2020', '110'], ['03-24-2020', '130'], ['03-25-2020', '160'], ['03-26-2020', '200']]
    len_row = len(row)
    for index, current in enumerate(row[::-1]):
        if index < len_row - 1:
            prev = row[len_row - index - 2]
            diff = int(current[1]) - int(prev[1])
            row[len_row - index - 1][1] = str(diff)
    return row
