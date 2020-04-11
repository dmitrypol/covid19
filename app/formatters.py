''' formatting data for models '''
# pylint: disable = eval-used, unused-variable
import pandas as pd


def last_confirmed(objs):
    output = 0
    for obj in objs:
        key = obj.confirmed.keys()[-1]
        output += int(obj.confirmed[key])
    return "{:,}".format(output)


def last_deaths(objs):
    output = 0
    for obj in objs:
        key = obj.deaths.keys()[-1]
        output += int(obj.deaths[key])
    return "{:,}".format(output)


def format_chart_data(objs):
    confirmed_out = _pandas_sum_hashes(objs, 'confirmed')
    deaths_out = _pandas_sum_hashes(objs, 'deaths')
    return {
        'confirmed':_row_date_diff(confirmed_out),
        'deaths':_row_date_diff(deaths_out),
        }


def _pandas_sum_hashes(objs, method):
    dfrm = pd.DataFrame()
    output = []
    for obj in objs:
        data = dict(eval(f'obj.{method}'))
        #   convert to int from str
        for key, value in data.items():
            data[key] = int(value)
        dfrm = dfrm.append(data, ignore_index=True)
    #   sum rows in dfrm
    sum_rows = dict(dfrm.sum())
    #   format data for chart
    for item in sorted(sum_rows.items()):
        output.append(list(item))
    return output


def _row_date_diff(row):
    #   [['03-22-2020', '100'], ['03-23-2020', '110'], ['03-24-2020', '130'], ['03-25-2020', '160'], ['03-26-2020', '200']]
    len_row = len(row)
    for index, current in enumerate(row[::-1]):
        if index < len_row - 1:
            prev = row[len_row - index - 2]
            diff = int(current[1]) - int(prev[1])
            row[len_row - index - 1][1] = int(diff)
    return row
