import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Freehand_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("A simple paint program")

        self.clear_button = QPushButton('Clear')
        self.clear_button.clicked.connect(Clear_Screen)

    def Clear_Screen(self):
        print('Clear')
      

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Freehand_window()
    window.show()
    app.exec_()
    sys.exit(0)