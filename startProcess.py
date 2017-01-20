from PyQt5.QtCore import QPoint, QSize, Qt, QTime, QTimer,QProcess
from PyQt5.QtGui import QColor, QPainter, QPolygon, QRegion
from PyQt5.QtWidgets import QAction, QApplication, QWidget

class ShapedClock(QWidget):
    def __init__(self, parent=None):
        super(ShapedClock, self).__init__(parent,
                Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)
        print("__init__")

        self.process = QProcess(self)
        self.process.start('HMD_Render.bat')
if __name__ == '__main__':
    import sys

    print('main')
    app = QApplication(sys.argv)
    clock = ShapedClock()
    clock.show()
    sys.exit(app.exec_())
