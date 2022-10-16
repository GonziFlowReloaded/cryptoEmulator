from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys
from datos import btcLastPrice

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        loadUi('gui.ui', self)
        self.labelUsdt.setText('0')
        self.labelBtc.setText('0')
        self.usdt = 0
        self.btc = 0
        
        
        
        self.show()
    
    def usdtToBtc(self):
        self.btc = self.usdt / btcLastPrice
        self.labelBtc.setText(str(self.btc))
    
    def btcToUsdt(self):
        self.usdt = self.btc * btcLastPrice
        self.labelUsdt.setText(str(self.usdt))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    
