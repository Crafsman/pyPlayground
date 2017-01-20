
#http://blog.csdn.net/caoshangpa/article/details/51037427
from PyQt5.QtCore import QPoint, QSize, Qt, QTime, QTimer,QProcess
from PyQt5.QtGui import QColor, QPainter, QPolygon, QRegion
from PyQt5.QtWidgets import QAction, QApplication, QWidget,QSplashScreen

class CMySplashScreen(QSplashScreen):
    def __init__(self, parent=None):
        super(CMySplashScreen, self).__init__(parent)
        print("CMySplashScreen__init__")



if __name__ == '__main__':
    import sys

    print('main')
    app = QApplication(sys.argv)
    clock = CMySplashScreen()
    clock.show()
    sys.exit(app.exec_())
