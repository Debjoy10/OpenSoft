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
import re

clicked_num = []
def calc(a, b, s):
	p = 0
	q = 0
	a_div = 0
	a_flag = False

	b_div = 0
	b_flag = False

	for i in a:
		if i=='.':
			a_flag = True
			continue
		if a_flag:
			a_div+=1
		p = (p*10+float(i))/(10**a_div)

	for i in b:
		if i=='.':
			b_flag = True
			continue
		if b_flag:
			b_div+=1
		q = (q*10+float(i))/(10**b_div)

	if s=="+":
		return str(p+q)
	if s=="-":
		return str(p-q)
	if s=="*":
		return str(p*q)
	if s=="/":
		return str(p/q)


def evaluate(clicked_num):
	nums = []
	ops = []
	currstr = []
	for sym in clicked_num:
		if sym in ["*", "+", "-", "/"]:
			ops.append(sym)
			nums.append(currstr)
			currstr = []
		else:
			currstr.append(sym)
	nums.append(currstr)
	currstr = []
	while len(nums)>1:
		a = nums[len(nums)-2]
		b = nums[len(nums)-1]
		s = ops[len(ops)-1]
		res = calc(a, b, s)
		nums = nums[0:len(nums)-2]
		nums.append(res)

	clicked_num.clear()
	clicked_num.append(res)
	text = ''.join(clicked_num)
	display.setText(text)

def dispnum():
	text = ''.join(clicked_num)
	display.setText(text)

def one():
	clicked_num.append("1")
	dispnum()
def two():
	clicked_num.append("2")
	dispnum()
def three():
	clicked_num.append("3")
	dispnum()
def four():
	print(clicked_num)
	clicked_num.append("4")
	dispnum()
def five():
	clicked_num.append("5")
	dispnum()
def six():
	clicked_num.append("6")
	dispnum()
def seven():
	clicked_num.append("7")
	dispnum()
def eight():
	clicked_num.append("8")
	dispnum()
def nine():
	clicked_num.append("9")
	dispnum()
def zero():
	clicked_num.append("0")
	dispnum()
def add():
	clicked_num.append("+")
	dispnum()
def subtract():
	clicked_num.append("-")
	dispnum()
def multiply():
	clicked_num.append("*")
	dispnum()
def divide():
	clicked_num.append("/")
	dispnum()
def point():
	clicked_num.append(".")
	dispnum()
def equals():
	evaluate(clicked_num)
def shut():
	sys.exit(app.exec_())
def C():
	clicked_num.clear()
	dispnum()
	

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
layout.addWidget(btn1, 2, 0)

btn1 = QPushButton('2')
btn1.clicked.connect(two)
layout.addWidget(btn1, 2, 1)

btn1 = QPushButton('3')
btn1.clicked.connect(three)
layout.addWidget(btn1, 2, 2)

btn1 = QPushButton('4')
btn1.clicked.connect(four)
layout.addWidget(btn1, 3, 0)

btn1 = QPushButton('5')
btn1.clicked.connect(five)
layout.addWidget(btn1, 3, 1)

btn1 = QPushButton('6')
btn1.clicked.connect(six)
layout.addWidget(btn1, 3, 2)

btn1 = QPushButton('7')
btn1.clicked.connect(seven)
layout.addWidget(btn1, 4, 0)

btn1 = QPushButton('8')
btn1.clicked.connect(eight)
layout.addWidget(btn1, 4, 1)

btn1 = QPushButton('9')
btn1.clicked.connect(nine)
layout.addWidget(btn1, 4, 2)

btn1 = QPushButton('0')
btn1.clicked.connect(zero)
layout.addWidget(btn1, 5, 0)

btn1 = QPushButton('+')
btn1.clicked.connect(add)
layout.addWidget(btn1, 2, 3)

btn1 = QPushButton('-')
btn1.clicked.connect(subtract)
layout.addWidget(btn1, 3, 3)

btn1 = QPushButton('*')
btn1.clicked.connect(multiply)
layout.addWidget(btn1, 4, 3)

btn1 = QPushButton('/')
btn1.clicked.connect(divide)
layout.addWidget(btn1, 5, 3)

btn1 = QPushButton('=')
btn1.clicked.connect(equals)
layout.addWidget(btn1, 5, 2)

btn1 = QPushButton('.')
btn1.clicked.connect(point)
layout.addWidget(btn1, 5, 1)

btn1 = QPushButton('C')
btn1.clicked.connect(C)
layout.addWidget(btn1, 1, 0, 1, 2)

btn1 = QPushButton('OFF')
btn1.clicked.connect(shut)
layout.addWidget(btn1, 1, 2, 1, 2)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
