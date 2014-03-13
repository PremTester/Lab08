import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Freehand_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.setWindowTitle("A simple paint program")

        layout = QVBoxLayout(self)

    
        self.Label = QLabel("Drag the mouse to draw")
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect( self.clear_image )
        self.animation_area = Animation_area()

        layout.addWidget(self.animation_area)
        
        layout.addWidget(self.Label)
        layout.addWidget(self.clear_button)

        self.setLayout( layout )

    def clear_image(self):
        self.animation_area.list.clear()



class Animation_area(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.list = []


        self.setMinimumSize(500, 500)

        self.arena_w = 500
        self.arena_h = 500
     

        timer = QTimer(self)
        self.connect(timer, SIGNAL("timeout()"), self.update_value)
        timer.start(500)

    def mousePressEvent(self, e):
        
        
        self.list.append( Dot(e.pos().x(), e.pos().y()) )
        print("Press")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setPen( QColor(0,0,0))
        
        for i in self.list:
            p.drawPolygon([
                           QPoint( i.x , i.y ), QPoint( i.x + 5, i.y),
                           QPoint( i.x, i.y + 5), QPoint( i.x, i.y + 5),
                            ])


        p.end()

    def mouseMoveEvent(self, e):
        self.list.append( Dot(e.pos().x(), e.pos().y()) )


    def update_value(self):
    
        self.update()

class Dot():

    def __init__(self, x, y):
        self.x = x
        self.y = y


 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Freehand_window()
    window.show()
    app.exec_()
    sys.exit(0)