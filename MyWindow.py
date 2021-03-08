from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def button_clicked(self):
        buttonname = self.sender()
        self.label.setText(buttonname.text())
        print(buttonname.text())

    def initUI(self):
        self.setGeometry(400, 200, 300, 300)
        self.setWindowTitle("Tech With Tim")

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(50,50,150,30)
        self.label.setText("my first label!")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("this is button 1 click me!")
        self.b1.setGeometry(100,100,150,30)
        self.b1.clicked.connect(self.button_clicked)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("this is button 2 click me!")
        self.b2.setGeometry(0, 0, 150, 30)
        self.b2.clicked.connect(self.button_clicked)


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()