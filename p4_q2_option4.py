from PySide import QtCore, QtGui
from p4_q2_ui import *
from library import *
import re

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
		self.nameOrId.returnPressed.connect(self.search)
		hBoxSearch.addWidget(self.nameOrId, 1)
		self.searchButton = QtGui.QPushButton('Search')
		self.searchButton.clicked.connect(self.search)
		hBoxSearch.addWidget(self.searchButton)
		layout.addLayout(hBoxSearch)
		searchResultsGroup = QtGui.QGroupBox('Search results')
		searchResultsLayout = QtGui.QVBoxLayout()
		self.searchResultsLabel = QtGui.QLabel('Ready.')
		searchResultsLayout.addWidget(self.searchResultsLabel, 0, QtCore.Qt.AlignCenter)
		self.searchResultsTable = QtGui.QTreeWidget()
		searchResultsLayout.addWidget(self.searchResultsTable, 1)
		self.searchResultsTable.setColumnCount(1)
		self.searchResultsTable.setHeaderLabels(['Name', 'Email', 'Address'])
		self.searchResultsTable.itemSelectionChanged.connect(self.changeResult)
		self.searchResultsTable.hide()
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
		self.status = QtGui.QLabel()
		layout.addWidget(self.status, 0, QtCore.Qt.AlignCenter)
		self.submitButton = QtGui.QPushButton('Change password')
		self.submitButton.clicked.connect(self.changePassword)
		layout.addWidget(self.submitButton, 0, QtCore.Qt.AlignCenter)
		self.passwordChangeFields = [currentPasswordLabel, self.currentPassword, currentSaltLabel, self.currentSalt, newPasswordLabel, self.newPassword, newSaltLabel, self.newSalt, self.status, self.submitButton]
		self.enableFields(False)
		self.results = []
	def enableFields(self, enabled=True):
		for f in self.passwordChangeFields:
			f.setEnabled(enabled)
		self.status.setText(u'')
	def search(self):
		self.enableFields(False)
		searchTerms = self.nameOrId.text()
		if not len(searchTerms):
			self.searchResultsTable.hide()
			self.searchResultsLabel.show()
			self.searchResultsLabel.setText('Ready.')
			return
		try:
			if re.match(r'\d+', searchTerms): # It's a user ID search
				sqlResult = sqlQuery('SELECT * FROM `people` WHERE `pnid` = ' + searchTerms + ' LIMIT 1', asDict=True).fetchall()
			else: # It's a name search
				conditions = ["`name` REGEXP '" + x.replace('\\', '\\\\').replace('\'', '\\\'') + "'" for x in searchTerms.split(' ')]
				sqlResult = sqlQuery('SELECT * FROM `people` WHERE ' + ' AND '.join(conditions), asDict=True).fetchall()
		except Exception, e:
			self.status.setText(unicode(e))
			return
		if not len(sqlResult):
			self.searchResultsTable.hide()
			self.searchResultsLabel.show()
			self.searchResultsLabel.setText('No results found!')
			return
		self.results = peopleTable.fromResults(sqlResult)
		self.searchResultsTable.clear()
		for p in self.results:
			self.searchResultsTable.addTopLevelItem(QtGui.QTreeWidgetItem([p['name'], p['email'], p['address']]))
		self.searchResultsLabel.hide()
		self.searchResultsTable.show()
		self.searchResultsTable.setCurrentItem(self.searchResultsTable.itemAt(0, 0))
	def getCurrentPerson(self):
		return self.results[self.searchResultsTable.indexFromItem(self.searchResultsTable.currentItem()).row()]
	def changeResult(self):
		self.enableFields(True)
		person = self.getCurrentPerson()
		self.currentPassword.setText(person['password'])
		self.currentSalt.setText(person['salt'])
		self.newPassword.setText('')
		self.newSalt.setText(person['salt'])
	def changePassword(self):
		if not self.newPassword.text():
			self.status.setText('Password cannot be empty.')
			return
		if not re.match(r'[a-fA-F\d]{32}', self.newSalt.text()):
			self.status.setText('Salt must be a 32-character hex string.')
			return
		person = self.getCurrentPerson()
		person.changePassword(self.newPassword.text(), self.newSalt.text())
		try:
			person.sync()
			self.changeResult()
			self.status.setText('Password changed!')
		except Exception, e:
			self.status.setText(unicode(e))


if __name__ == '__main__':
	runApp(3)
