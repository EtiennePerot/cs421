from PySide import QtCore, QtGui
from p4_q2_ui import *

class Option1(UIOption):
	def __init__(self):
		UIOption.__init__(self)
	def getTitle(self):
		return 'Option 1'
	def initUI(self, layout):
		layout.addWidget(QtGui.QLabel('This is option 1'))
