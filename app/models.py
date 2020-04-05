''' varous models '''
# pylint: disable = no-self-use
from walrus import Model, TextField, HashField
from . import WALRUS_DB


class Location(Model):
    __database__ = WALRUS_DB
    # __namespace__ = 'my-app'
    name = TextField(primary_key=True)
    county = TextField(index=False)
    state = TextField(index=False)
    country = TextField(index=False)
    confirmed = HashField()
    deaths = HashField()


    def last_confirmed(self):
        key = self.confirmed.keys()[-1]
        return self.confirmed[key]


    def last_deaths(self):
        key = self.deaths.keys()[-1]
        return self.deaths[key]


    def format_chart_data(self):
        confirmed = []
        for item in sorted(self.confirmed.items()):
            confirmed.append(list(item))
        deaths = []
        for item in sorted(self.deaths.items()):
            deaths.append(list(item))
        return {
            'confirmed':self._row_date_diff(confirmed),
            'deaths':self._row_date_diff(deaths),
            }


    def _row_date_diff(self, row):
        #   [['03-22-2020', '100'], ['03-23-2020', '110'], ['03-24-2020', '130'], ['03-25-2020', '160'], ['03-26-2020', '200']]
        len_row = len(row)
        for index, current in enumerate(row[::-1]):
            if index < len_row - 1:
                prev = row[len_row - index - 2]
                diff = int(current[1]) - int(prev[1])
                row[len_row - index - 1][1] = str(diff)
        return row
