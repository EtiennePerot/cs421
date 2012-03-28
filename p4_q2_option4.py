from PySide import QtCore, QtGui
from p4_q2_ui import *

class Option4(UIOption):
	def __init__(self):
		UIOption.__init__(self, True)
	def getTitle(self):
		return 'Password reset'
	def initUI(self, layout):
		layout.addWidget(QtGui.QLabel('This option allows you to reset a user\'s password.'))
		hBoxSearch = QtGui.QHBoxLayout()
		hBoxSearch.addWidget(QtGui.QLabel('<strong>Name or ID</strong>: '))
		self.nameOrId = QtGui.QLineEdit()
		self.nameOrId.setPlaceholderText('Name or ID...')
		hBoxSearch.addWidget(self.nameOrId, 1)
		self.searchButton = QtGui.QPushButton('Search')
		hBoxSearch.addWidget(self.searchButton)
		layout.addLayout(hBoxSearch)
		searchResultsGroup = QtGui.QGroupBox('Search results')
		searchResultsLayout = QtGui.QVBoxLayout()
		self.searchResultsLabel = QtGui.QLabel('Ready.')
		searchResultsLayout.addWidget(self.searchResultsLabel, 0, QtCore.Qt.AlignCenter)
		searchResultsGroup.setLayout(searchResultsLayout)
		layout.addWidget(searchResultsGroup, 1)
		currentLayout = QtGui.QHBoxLayout()
		currentPasswordLayout = QtGui.QVBoxLayout()
		currentSaltLayout = QtGui.QVBoxLayout()
		currentLayout.addLayout(currentPasswordLayout, 1)
		currentLayout.addLayout(currentSaltLayout, 1)
		currentPasswordLabel = QtGui.QLabel('<strong>Current hashed password</strong>:')
		currentPasswordLayout.addWidget(currentPasswordLabel)
		self.currentPassword = QtGui.QLineEdit()
		self.currentPassword.setReadOnly(True)
		currentPasswordLayout.addWidget(self.currentPassword)
		currentSaltLabel = QtGui.QLabel('<strong>Current salt</strong>:')
		currentSaltLayout.addWidget(currentSaltLabel)
		self.currentSalt = QtGui.QLineEdit()
		self.currentSalt.setReadOnly(True)
		currentSaltLayout.addWidget(self.currentSalt)
		layout.addLayout(currentLayout)
		newLayout = QtGui.QHBoxLayout()
		newPasswordLayout = QtGui.QVBoxLayout()
		newSaltLayout = QtGui.QVBoxLayout()
		newLayout.addLayout(newPasswordLayout, 1)
		newLayout.addLayout(newSaltLayout, 1)
		newPasswordLabel = QtGui.QLabel('<strong>New password</strong>:')
		newPasswordLayout.addWidget(newPasswordLabel)
		self.newPassword = QtGui.QLineEdit()
		self.newPassword.setPlaceholderText('Password...')
		self.newPassword.setEchoMode(QtGui.QLineEdit.Password)
		newPasswordLayout.addWidget(self.newPassword)
		newSaltLabel = QtGui.QLabel('<strong>New salt</strong>:')
		newSaltLayout.addWidget(newSaltLabel)
		self.newSalt = QtGui.QLineEdit()
		self.newSalt.setPlaceholderText('Salt...')
		newSaltLayout.addWidget(self.newSalt)
		layout.addLayout(newLayout)
		self.submitButton = QtGui.QPushButton('Change password')
		layout.addWidget(self.submitButton, 0, QtCore.Qt.AlignCenter)
		self.passwordChangeFields = [currentPasswordLabel, self.currentPassword, currentSaltLabel, self.currentSalt, newPasswordLabel, self.newPassword, newSaltLabel, self.newSalt, self.submitButton]
		self.enableFields(False)
	def enableFields(self, enabled=True):
		for f in self.passwordChangeFields:
			f.setEnabled(enabled)

if __name__ == '__main__':
	runApp(3)
