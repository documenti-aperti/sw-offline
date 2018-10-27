#Libraries
import sys
from PyQt5.QtWidgets import QApplication

#Pythons
from mainwindow import MainWindow

if __name__ == '__main__':
    App = QApplication(sys.argv)
    screen_size = App.desktop().screenGeometry()
    window = MainWindow(screen_size.width(), screen_size.height())
    sys.exit(App.exec_())
