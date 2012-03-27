import sys
from PySide import QtCore, QtGui

class UIOption(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self._layout = QtGui.QVBoxLayout()
		self._continueButton = QtGui.QPushButton('Run!')
		self._layout.addWidget(self._continueButton, 0, QtCore.Qt.AlignCenter)
		self.setLayout(self._layout)
		self._continueButton.clicked.connect(self.run)
	def getTitle(self):
		return 'Untitled option'
	def run(self):
		self._continueButton.hide()
		self.initUI(self._layout)
	def initUI(self, layout):
		pass

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	tabs = QtGui.QTabWidget()
	tabs.setWindowTitle('COMP 421 - Project Milestone 4 - Group 32')
	tabs.setMinimumSize(640, 480)
	from p4_q2_option1 import Option1
	option1 = Option1()
	tabs.addTab(option1, option1.getTitle())
	from p4_q2_option2 import Option2
	option2 = Option2()
	tabs.addTab(option2, option2.getTitle())
	from p4_q2_option3 import Option3
	option3 = Option3()
	tabs.addTab(option3, option3.getTitle())
	from p4_q2_option4 import Option4
	option4 = Option4()
	tabs.addTab(option4, option4.getTitle())
	from p4_q2_option5 import Option5
	option5 = Option5()
	tabs.addTab(option5, option5.getTitle())
	tabs.show()
	sys.exit(app.exec_())
