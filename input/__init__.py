import pandas as pd

# print('F',  __file__)

import pathlib
import os


dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
# __data = pd.read_csv(os.path.dirname(__file__) + '/' + 'AirPassengers.csv', parse_dates=['Month'], index_col='Month',date_parser=dateparse)
__data = pd.read_csv(pathlib.Path(os.path.dirname(__file__)) / 'AirPassengers.csv', parse_dates=['Month'], index_col='Month',date_parser=dateparse)
__data.head()

air_passengers = __data
data = __data
asdataframe = __data
aslist = list(data.as_matrix()[:, 0])