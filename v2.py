import imp
from turtle import pensize
from webbrowser import get
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import mplfinance as mpf
import datetime as dt
from pandas_datareader import data as datatex
import yfinance as yf
import sys
import pyqtgraph as pg

import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np
import websocket
import json
import threading
import time



class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        loadUi('gui2.ui', self)
        self.timer = QTimer()
        self.tiempo = 0
        self.listAux = []
        self.listaTiempo = []
        
        #-----------------ini Labels-----------------#
        self.labelUsdt.setText('1000')
        self.labelBtc.setText('0')
        self.usdt = 1000
        self.btc = 0
        
        #-----------------ini Buttons-----------------#
        self.botonComprar.clicked.connect(self.usdtToBtc)
        self.botonVender.clicked.connect(self.btcToUsdt)
        
        #-----------------ini data-----------------#
        yf.pdr_override()

        self.y_simbolo = 'BTC-USD'
        self.y_inicio = '2022-01-01'
        self.y_fin = dt.datetime.now()
        
        data = datatex.get_data_yahoo(self.y_simbolo, start=self.y_inicio, end=self.y_fin)

        #-----------------ini Grafica-----------------#
        colors = mpf.make_marketcolors(up='g', down='r', edge='inherit', wick='inherit', volume='in')
        mpf_style = mpf.make_mpf_style(base_mpf_style='nightclouds', marketcolors=colors)
        
        # self.grafica = mpf.plot(data=data, type='candle', style=mpf_style, volume=True, title='BTC/USD', ylabel='Precio (USDT)', ylabel_lower='Volumen')
        self.grafica = pg.PlotWidget()
        self.grafica.setBackground('black')
        self.grafica.showGrid(x=True, y=True)
        self.grafica.setLabel('left', 'Precio', units='USDT')

        

        self.timer = QTimer()

        self.timer.timeout.connect(self.update)
        time.sleep(4)
        self.timer.start(1000)

        
        
        self.groupBoxGrafica.layout().addWidget(self.grafica)
        
        



        
        
        self.show()


    def update(self):
        global btcLastPrice
        
        self.listAux.append(btcLastPrice)
        self.listaTiempo.append(self.tiempo)
        self.grafica.plotItem.clear()
        self.grafica.plot(self.listaTiempo, self.listAux, pen='g', pensize=3)
        self.tiempo += 1
        

        




    def usdtToBtc(self):
        
        global btcLastPrice
        
        try:
            if self.usdt == 0:
                pass
            else:
                self.btc = self.usdt / btcLastPrice
                self.usdt = 0
                self.labelUsdt.setText(str(self.usdt))
                self.labelBtc.setText(str(self.btc))
        except:
            print("Error")
        
    
    def btcToUsdt(self):
        global btcLastPrice
        if self.btc == 0:
            pass
        else:
            self.usdt = self.btc * btcLastPrice
            self.btc = 0
            self.labelBtc.setText(str(self.btc))
            self.labelUsdt.setText(str(self.usdt))

SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m"
btcLastPrice = 0

def on_open(ws):
    print("opened connection")

def on_close(ws):
    print("closed connection")

def on_message(ws, message):
    json_message = json.loads(message)
    #pprint.pprint(json_message)
    #Show last price
    #print("Ultimo precio: ", json_message["k"]["c"])
    global btcLastPrice 
    btcLastPrice = float(json_message["k"]["c"])

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
def printBtcPrice():
    time.sleep(4)
    while True:
        time.sleep(1)
        print("Precio de BTC funcion aparte: ", btcLastPrice)
    

#get current price
def getBtcPrice():
    hilo1 = threading.Thread(target=ws.run_forever)
    hilo2 = threading.Thread(target=printBtcPrice)
    

    hilo1.start()
    hilo2.start()






if __name__ == '__main__':
    getBtcPrice()
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    
