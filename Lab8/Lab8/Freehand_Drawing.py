import sys
from PySide.QtCore import *
from PySide.QtGui import *

class freehand_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.setWindowTitle("a simple paint program")

        layout = QVBoxLayout(self)

    
        self.label = QLabel("drag the mouse to draw")
        self.clear_button = QPushButton("clear")
        self.clear_button.clicked.connect( self.clear_image )
        self.animation_area = animation_area()

        layout.addWidget(self.animation_area)
        
        layout.addWidget(self.label)
        layout.addWidget(self.clear_button)

        self.setLayout( layout )

    def clear_image(self):
        self.animation_area.list.clear()



class animation_area(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.list = []

        self.image = QImage("images/dot.png")
        self.setMinimumSize(500, 500)

        self.arena_w = 500
        self.arena_h = 500
     

        self.timer = QTimer(self)
        self.timer.timeout.connect( self.update_value )
        self.timer.start(30)


    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.setPen( QColor(0,0,0))
        
        p.drawPoints( self.list )


        p.end()

    def mouseMoveEvent(self, e):
        self.list.append( e.pos() )


    def update_value(self):
    
        self.update()

class dot():

    def __init__(self, x, y):
        self.x = x
        self.y = y


 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = freehand_window()
    window.show()
    app.exec_()
    sys.exit(0)


