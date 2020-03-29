''' jobs '''
# pylint: disable = pointless-string-statement
import logging
from datetime import datetime, timedelta
import pandas as pd
# from walrus import Database
from . import APP, RQ_CLIENT

BASE_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports'
# WDB = Database(host=APP.config.get('REDIS_HOST'), port=6379, db=3)
REDIS_CLIENT = APP.config.get('REDIS_CLIENT')


@RQ_CLIENT.job()
def import_data(date=(datetime.today() - timedelta(days=1)).strftime('%m-%d-%Y')):
    #   '03-22-2020'
    logging.info(f'import_data for {date}')
    url = f'{BASE_URL}/{date}.csv'
    dfrm = pd.read_csv(url)
    for _, row in dfrm.iterrows():
        _process_row(row)


def _process_row(row):
    if row.Country_Region == 'US':
        name = row.Combined_Key.replace(' ', '').replace(',', '')
        fdate = _format_date(row.Last_Update)
        mapping = {'county':row.Admin2, 'state':row.Province_State, 'country':row.Country_Region, fdate:row.Deaths}
        REDIS_CLIENT.hmset(name, mapping)
        # wal_hash = WDB.Hash(key)
        # wal_hash.update(date2=row.Deaths)


def _format_date(last_update):
    if '/' in last_update:
        output = datetime.strptime(last_update, '%m/%d/%y %H:%M').strftime('%m-%d-%Y')
    elif '-' in last_update:
        output = datetime.strptime(last_update, '%Y-%m-%d %H:%M:%S').strftime('%m-%d-%Y')
    return output


'''
FIPS                                      45001
Admin2                                Abbeville
Province_State                   South Carolina
Country_Region                               US
Last_Update                 2020-03-28 23:05:37
Lat                                     34.2233
Long_                                  -82.4617
Confirmed                                     3
Deaths                                        0
Recovered                                     0
Active                                        0
Combined_Key      Abbeville, South Carolina, US
Name: 0, dtype: object

FIPS                                      53023
Admin2                          Garfield County
Province_State                       Washington
Country_Region                               US
Last_Update                       3/22/20 23:45
Lat                                      46.452
Long_                                  -117.545
Confirmed                                     1
Deaths                                        2
Recovered                                     0
Active                                        0
Combined_Key      Garfield County,Washington,US
Name: 3416, dtype: object
'''