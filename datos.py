import imp
import time
import websocket
import json
import pprint
import threading

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


getBtcPrice()





