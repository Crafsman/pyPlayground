import sys
from PyQt5.QtCore import QPoint, QSize, Qt, QTime, QTimer, QRect, QCoreApplication, QMetaObject
from PyQt5.QtGui import QColor, QPainter, QPolygon, QRegion, QPainterPath, QPen
from PyQt5.QtWidgets import QAction, QApplication, QWidget, QPushButton
from math import pi, cos, sin



class Ui_heartWidget(object):
    def setupUi(self, heartWidget):
        heartWidget.setObjectName("heartWidget")
        heartWidget.resize(700, 700)
        heartWidget.setStyleSheet("border-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));")
        self.startButton = QPushButton(heartWidget)
        self.startButton.setGeometry(QRect(10, 10, 75, 23))
        self.startButton.setObjectName("startButton")
        self.stopButton = QPushButton(heartWidget)
        self.stopButton.setGeometry(QRect(100, 10, 75, 23))
        self.stopButton.setObjectName("stopButton")

        self.retranslateUi(heartWidget)
        self.startButton.clicked.connect(heartWidget.slot1)
        QMetaObject.connectSlotsByName(heartWidget)

    def retranslateUi(self, heartWidget):
        _translate = QCoreApplication.translate
        heartWidget.setWindowTitle(_translate("heartWidget", "qt_plagroud2015"))
        self.startButton.setText(_translate("heartWidget", "Start"))
        self.stopButton.setText(_translate("heartWidget", "End"))




class HeartPicture(QWidget):
    points = [] #to store the points
    pointsNum = 0
    index = 0
    mPath = QPainterPath()

    def __init__(self, parent = None):
        super(HeartPicture, self).__init__(parent)
        ui = Ui_heartWidget()
        ui.setupUi(self)

        for i in range(0, 90):
            for j in range(0, 90):
                r = pi / 45 * i * (1 - sin(pi / 45 * j)) * 40
                x = r * cos(pi / 45.0 * j) * sin(pi / 45.0 * i) + self.width() / 2
                y = -r * sin(pi / 45 * j) + self.height() / 4
                HeartPicture.points.append((x,y))

        HeartPicture.pointsNum = len(HeartPicture.points)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timerUpdate)


    def slot1(self):
        self.timer.start(1)

    def timerUpdate(self):
        self.update()
        if HeartPicture.index > HeartPicture.pointsNum -1:
            return
        HeartPicture.mPath.lineTo((HeartPicture.points[HeartPicture.index])[0],(HeartPicture.points[HeartPicture.index])[1])
        HeartPicture.index += 1

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.red, 1, Qt.DotLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawPath(HeartPicture.mPath)

    

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = HeartPicture()
    
   
    w.setWindowTitle('Simple')
    w.show()
    sys.exit(app.exec_())
