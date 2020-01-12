import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout

def evaluate():
	print("hi")

clicked_num = []
def one():
	clicked_num.append("1")
def two():
	clicked_num.append("2")
def three():
	clicked_num.append("3")
def four():
	clicked_num.append("4")
def five():
	clicked_num.append("5")
def six():
	clicked_num.append("6")
def seven():
	clicked_num.append("7")
def eight():
	clicked_num.append("8")
def nine():
	clicked_num.append("9")
def zero():
	clicked_num.append("0")
def add():
	clicked_num.append("+")
def subtract():
	clicked_num.append("-")
def multiply():
	clicked_num.append("*")
def divide():
	clicked_num.append("/")
def point():
	clicked_num.append(".")
def equals():
	evaluate()

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('My Calculator')
layout = QGridLayout()

display = QLineEdit()
display.setFixedHeight(30)
display.setAlignment(Qt.AlignRight)
display.setReadOnly(True)
layout.addWidget(display, 0, 0, 1, 4)

btn1 = QPushButton('1')
btn1.clicked.connect(one)
layout.addWidget(btn1, 1, 0)

btn1 = QPushButton('2')
btn1.clicked.connect(two)
layout.addWidget(btn1, 1, 1)

btn1 = QPushButton('3')
btn1.clicked.connect(three)
layout.addWidget(btn1, 1, 2)

btn1 = QPushButton('4')
btn1.clicked.connect(four)
layout.addWidget(btn1, 2, 0)

btn1 = QPushButton('5')
btn1.clicked.connect(five)
layout.addWidget(btn1, 2, 1)

btn1 = QPushButton('6')
btn1.clicked.connect(six)
layout.addWidget(btn1, 2, 2)

btn1 = QPushButton('7')
btn1.clicked.connect(seven)
layout.addWidget(btn1, 3, 0)

btn1 = QPushButton('8')
btn1.clicked.connect(eight)
layout.addWidget(btn1, 3, 1)

btn1 = QPushButton('9')
btn1.clicked.connect(nine)
layout.addWidget(btn1, 3, 2)

btn1 = QPushButton('0')
btn1.clicked.connect(zero)
layout.addWidget(btn1, 4, 0)

btn1 = QPushButton('+')
btn1.clicked.connect(add)
layout.addWidget(btn1, 1, 3)

btn1 = QPushButton('-')
btn1.clicked.connect(subtract)
layout.addWidget(btn1, 2, 3)

btn1 = QPushButton('*')
btn1.clicked.connect(multiply)
layout.addWidget(btn1, 3, 3)

btn1 = QPushButton('/')
btn1.clicked.connect(divide)
layout.addWidget(btn1, 4, 3)

btn1 = QPushButton('=')
btn1.clicked.connect(equals)
layout.addWidget(btn1, 4, 2)

btn1 = QPushButton('.')
btn1.clicked.connect(point)
layout.addWidget(btn1, 4, 1)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
