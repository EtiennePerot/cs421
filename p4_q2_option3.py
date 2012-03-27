from PySide import QtCore, QtGui
from p4_q2_ui import *

class Option3(UIOption):
	def __init__(self):
		UIOption.__init__(self)
	def getTitle(self):
		return 'Option 3'
	def initUI(self, layout):
		layout.addWidget(QtGui.QLabel('This is option 3'))
