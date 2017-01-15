import sys
from PyQt5.QtCore import QPoint, QSize, Qt, QTime, QTimer
from PyQt5.QtGui import QColor, QPainter, QPolygon, QRegion, QPainterPath, QPen
from PyQt5.QtWidgets import QAction, QApplication, QWidget
from math import pi, cos, sin


class HeartPicture(QWidget):

    points = [] #to store the points
    pointsNum = 0
    index = 0
    def showPoints(self):
        for i in HeartPicture.points:
            print(i)
            
    def __init__(self, parent = None):
        super(HeartPicture, self).__init__(parent)

        for i in range(0, 90):
            for j in range(0, 90):
                r = pi / 45 * i * (1 - sin(pi / 45 * j)) * 18
                x = r * cos(pi / 45.0 * j) * sin(pi / 45.0 * i) + self.width() / 2
                y = -r * sin(pi / 45 * j) + self.height() / 4
                HeartPicture.points.append((x,y))
 #       self.showPoints()       

        HeartPicture.pointsNum = len(HeartPicture.points)

        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(500)

    def paintEvent(self, event):

        self.update()
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.red, 3, Qt.DotLine))

        if HeartPicture.index > HeartPicture.pointsNum -1:
            #print('retrun')
            return

        polygonPath = QPainterPath()
 #       polygonPath.lineTo(140, 400)
 
        
        polygonPath.lineTo((HeartPicture.points[HeartPicture.index])[0],(HeartPicture.points[HeartPicture.index])[1])
        polygonPath.moveTo((HeartPicture.points[HeartPicture.index])[0],(HeartPicture.points[HeartPicture.index])[1])
        
        r = 10
        painter.drawEllipse(HeartPicture.points[HeartPicture.index][0], HeartPicture.points[HeartPicture.index][1], r, r)
        HeartPicture.index += 1
        painter.restore()
 #       painter.drawPath(polygonPath)
 
    
    #def update(self):
        #print('hello')
    
 



        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = HeartPicture()
    w.resize(500, 500)
   
    w.setWindowTitle('Simple')
    w.show()
    sys.exit(app.exec_())
