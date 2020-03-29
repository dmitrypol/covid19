''' jobs '''
# pylint: disable = pointless-string-statement
import logging
import pandas as pd
from . import RQ_CLIENT

BASE_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports'


@RQ_CLIENT.job()
def import_data(date='03-22-2020'):
    logging.info('import_data')
    url = f'{BASE_URL}/{date}.csv'
    dfrm = pd.read_csv(url)
    for _, row in dfrm.iterrows():
        process_row(row)


def process_row(row):
    if row.Country_Region == 'US':
        logging.info(f"{row['Admin2']} {row['Province_State']} {row['Confirmed']}")


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
'''