import websocket
import json
import pprint


SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m"

def on_open(ws):
    print("opened connection")

def on_close(ws):
    print("closed connection")

def on_message(ws, message):
    json_message = json.loads(message)
    pprint.pprint(json_message)
    #Show last price
    print("Ultimo precio: ", json_message["k"]["c"])
    btcLastPrice = float(json_message["k"]["c"])
    return btcLastPrice

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
btcLastPrice, asd = ws.run_forever()
print('aaa: '+asd)