#import sys
#from PySide.QtCore import *
#from PySide.QtGui import *

#class Freehand_window(QWidget):
#    def __init__(self):
#        QWidget.__init__(self, None)

#        self.setWindowTitle("A simple paint program")

#        layout = QVBoxLayout(self)

    
#        self.Label = QLabel("Drag the mouse to draw")
#        self.clear_button = QPushButton("Clear")
#        self.clear_button.clicked.connect( self.clear_image )
#        self.animation_area = Animation_area()

#        layout.addWidget(self.animation_area)
        
#        layout.addWidget(self.Label)
#        layout.addWidget(self.clear_button)

#        self.setLayout( layout )

#    def clear_image(self):
#        self.animation_area.list.clear()



#class Animation_area(QWidget):
#    def __init__(self):
#        QWidget.__init__(self, None)
#        self.list = []

#        self.image = QImage("images/dot.png")
#        self.setMinimumSize(500, 500)

#        self.arena_w = 500
#        self.arena_h = 500
     

#        timer = QTimer(self)
#        self.connect(timer, SIGNAL("timeout()"), self.update_value)
#        timer.start(500)

#    def mousePressEvent(self, e):
        
        
#        self.list.append( Dot(e.pos().x(), e.pos().y()) )
#        print("Press")

#    def paintEvent(self, e):
#        p = QPainter()
#        p.begin(self)
#        p.setPen( QColor(0,0,0))
        
#        for i in self.list:
#            p.drawImage(QRect(i.x, i.y, 10, 10), self.image)


#        p.end()

#    def mouseMoveEvent(self, e):
#        self.list.append( Dot(e.pos().x(), e.pos().y()) )


#    def update_value(self):
    
#        self.update()

#class Dot():

#    def __init__(self, x, y):
#        self.x = x
#        self.y = y


 

#if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    window = Freehand_window()
#    window.show()
#    app.exec_()
#    sys.exit(0)


import sys
from PySide.QtCore import *
from PySide.QtGui import *
 
class PaintWidget(QWidget):
    WINDOW_WIDTH = 300
    WINDOW_HEIGHT = 300
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUI()
        self.points = []
 
    def setupUI(self):
        self.setFixedSize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
 
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.begin(self)
        painter.drawPoints(self.points)
        painter.end()
 
    def mouseMoveEvent(self, e):
       self.points.append(e.pos())
       self.update()
 
class SimplePaintProgram(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUI()
 
 
    def setupUI(self):
        self.setWindowTitle("A Simple Paint Program")
 
        layout = QVBoxLayout()
       
        self.paintArea = PaintWidget()
        label = QLabel("Drag the mouse to draw")
        label.setAlignment(Qt.AlignHCenter)
        clearBt = QPushButton("Clear")
        clearBt.clicked.connect(self.test)
       
        layout.addWidget(self.paintArea)
        layout.addWidget(label)
        layout.addWidget(clearBt)
 
        self.setLayout(layout)
 
    def test(self):
        self.paintArea.points = []
        self.paintArea.update()
 
 
def main():
    app = QApplication(sys.argv)
    w = SimplePaintProgram()
    w.show()
    return app.exec_()
 
if __name__ == "__main__":
    sys.exit(main())