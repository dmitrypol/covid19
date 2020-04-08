''' formatting data for models '''
import pandas as pd


def last_confirmed(objs):
    output = 0
    for obj in objs:
        key = obj.confirmed.keys()[-1]
        output += int(obj.confirmed[key])
    return str(output)

def last_deaths(objs):
    output = 0
    for obj in objs:
        key = obj.deaths.keys()[-1]
        output += int(obj.deaths[key])
    return str(output)


def format_chart_data(objs):
    #   TODO - DRY up
    dfrm_con = pd.DataFrame()
    confirmed_out = []
    for obj in objs:
        confirmed = dict(obj.confirmed)
        for key, value in confirmed.items():
            confirmed[key] = int(value)
        dfrm_con = dfrm_con.append(confirmed, ignore_index=True)
    confirmed_sum = dict(dfrm_con.sum())
    for item in sorted(confirmed_sum.items()):
        confirmed_out.append(list(item))
    #
    dfrm_dea = pd.DataFrame()
    deaths_out = []
    for obj in objs:
        deaths = dict(obj.deaths)
        for key, value in deaths.items():
            deaths[key] = int(value)
        dfrm_dea = dfrm_dea.append(deaths, ignore_index=True)
    deaths_sum = dict(dfrm_dea.sum())
    for item in sorted(deaths_sum.items()):
        deaths_out.append(list(item))
    #
    return {
        'confirmed':_row_date_diff(confirmed_out),
        'deaths':_row_date_diff(deaths_out),
        }


def _row_date_diff(row):
    #   [['03-22-2020', '100'], ['03-23-2020', '110'], ['03-24-2020', '130'], ['03-25-2020', '160'], ['03-26-2020', '200']]
    len_row = len(row)
    for index, current in enumerate(row[::-1]):
        if index < len_row - 1:
            prev = row[len_row - index - 2]
            diff = int(current[1]) - int(prev[1])
            row[len_row - index - 1][1] = int(diff)
    return row
