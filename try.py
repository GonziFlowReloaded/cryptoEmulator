import mplfinance as mpf
import datetime as dt
from pandas_datareader import data as datatex
import yfinance as yf

yf.pdr_override()

y_simbolo = 'BTC-USD'
y_inicio = '2022-01-01'
y_fin = dt.datetime.now()

data = datatex.get_data_yahoo(y_simbolo, start=y_inicio, end=y_fin)

colors = mpf.make_marketcolors(up='g', down='r', edge='inherit', wick='inherit', volume='in')

mpf_style = mpf.make_mpf_style(base_mpf_style='nightclouds', marketcolors=colors)

mpf.plot(data=data, type='candle', style=mpf_style, volume=True, title='BTC/USD', ylabel='Precio (USDT)', ylabel_lower='Volumen')
