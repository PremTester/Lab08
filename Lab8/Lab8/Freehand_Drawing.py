import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Freehand_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Freehand_Drawing")
        self.setMinimumHeight(100)
        self.setMinimumWidth(250)
        self.setMaximumHeight(200)
        self.setMaximumWidth(800)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Freehand_window()
    window.show()
    app.exec_()
    sys.exit(0)