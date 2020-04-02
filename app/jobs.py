''' jobs '''
# pylint: disable = pointless-string-statement
import logging, urllib
from datetime import datetime, timedelta
import pandas as pd
from . import RQ_CLIENT, models

BASE_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports'


@RQ_CLIENT.job()
def import_data(date=(datetime.today() - timedelta(days=0)).strftime('%m-%d-%Y')):
    #   'MM-DD-YYYY'
    logging.info(f'import_data for {date}')
    url = f'{BASE_URL}/{date}.csv'
    try:
        dfrm = pd.read_csv(url)
        for _, row in dfrm.iterrows():
            _process_row(row)
    except urllib.error.HTTPError:
        pass


def _process_row(row):
    if row.Country_Region == 'US' and pd.notnull(row.Admin2):
        name = row.Combined_Key.replace(' ', '').replace(',', '')
        fdate = _format_date(row.Last_Update)
        obj = models.Location.create(name=name, county=row.Admin2, state=row.Province_State, country=row.Country_Region)
        obj.confirmed.update({fdate:row.Confirmed})
        obj.deaths.update({fdate:row.Deaths})
        obj.save()


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