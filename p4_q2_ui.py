import sys
from PySide import QtCore, QtGui

class UIOption(QtGui.QWidget):
	def __init__(self, autoload=False):
		QtGui.QWidget.__init__(self)
		self._outerLayout = QtGui.QVBoxLayout(self)
		self._scrollBox = QtGui.QScrollArea(self)
		self._scrollBox.setFrameShape(QtGui.QFrame.NoFrame)
		self._outerLayout.addWidget(self._scrollBox, 1)
		self._scrollWidget = QtGui.QWidget(self._scrollBox)
		self._scrollBox.setWidget(self._scrollWidget)
		self._scrollBox.setWidgetResizable(True)
		self._layout = QtGui.QVBoxLayout(self._scrollWidget)
		self._scrollWidget.setLayout(self._layout)
		if autoload:
			self.initUI(self._layout)
		else:
			self._continueButton = QtGui.QPushButton('Run!', self._scrollWidget)
			self._layout.addWidget(self._continueButton, 0, QtCore.Qt.AlignCenter)
			self._continueButton.clicked.connect(self.run)
		self.setLayout(self._outerLayout)
	def getTitle(self):
		return 'Untitled option'
	def run(self):
		self._continueButton.deleteLater()
		self.initUI(self._layout)
	def initUI(self, layout):
		pass

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	tabs = QtGui.QTabWidget()
	tabs.setWindowTitle('COMP 421 - Project Milestone 4 - Group 32')
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
