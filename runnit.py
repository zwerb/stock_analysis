#Import the libraries
import math
#import pandas_datareader as web
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')#

DATADIR = 'stock_files'
GRAPHDIR = '../html/images/stock_graphs/'
SPLITSDIR = 'split_files'

import sa_functions as sa

ticker = raw_input("Type a ticker: ")
days_range = raw_input("Input days: ") 
sa.online_process_stock_once(str(ticker), int(days_range))