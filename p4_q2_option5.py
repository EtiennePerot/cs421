from PySide import QtCore, QtGui
from p4_q2_ui import *
from library import *
import re

class Option5(UIOption):
	def __init__(self):
		UIOption.__init__(self, True)
	def getTitle(self):
		return 'Search by author'
	def initUI(self, layout):
		layout.addWidget(QtGui.QLabel('This option allows you to search the database by author.'))
		authorSearchLayout = QtGui.QHBoxLayout()
		authorSearchLayout.addWidget(QtGui.QLabel('<strong>Author name or ID</strong>: '))
		self.nameOrId = QtGui.QLineEdit()
		self.nameOrId.setPlaceholderText('Name or ID...')
		self.nameOrId.returnPressed.connect(self.search)
		authorSearchLayout.addWidget(self.nameOrId, 1)
		self.searchButton = QtGui.QPushButton('Search')
		self.searchButton.clicked.connect(self.search)
		authorSearchLayout.addWidget(self.searchButton)
		layout.addLayout(authorSearchLayout)
		searchResultsGroup = QtGui.QGroupBox('Author matches')
		searchResultsLayout = QtGui.QVBoxLayout()
		self.searchResultsLabel = QtGui.QLabel('Ready.')
		searchResultsLayout.addWidget(self.searchResultsLabel, 0, QtCore.Qt.AlignCenter)
		self.searchResultsList = QtGui.QListWidget()
		searchResultsLayout.addWidget(self.searchResultsList, 1)
		self.searchResultsList.itemSelectionChanged.connect(self.changeAuthor)
		self.searchResultsList.hide()
		searchResultsGroup.setLayout(searchResultsLayout)
		layout.addWidget(searchResultsGroup, 1)
		self.status = QtGui.QLabel()
		layout.addWidget(self.status, 0, QtCore.Qt.AlignCenter)
		itemsGroup = QtGui.QGroupBox('Item matches')
		itemsLayout = QtGui.QVBoxLayout()
		itemsGroup.setLayout(itemsLayout)
		self.itemsLabel = QtGui.QLabel('Nothing to see here.')
		itemsLayout.addWidget(self.itemsLabel, 0, QtCore.Qt.AlignCenter)
		self.itemsList = QtGui.QTreeWidget()
		self.itemsList.setColumnCount(3)
		self.itemsList.setHeaderLabels(['Title', 'Type', 'Date'])
		itemsLayout.addWidget(self.itemsList, 1)
		self.itemsList.hide()
		layout.addWidget(itemsGroup, 3)
		self.authors = []
	def search(self):
		# Reset items group
		self.itemsLabel.show()
		self.itemsList.hide()
		self.itemsLabel.setText('Nothing to see here.')
		searchTerms = self.nameOrId.text()
		if not len(searchTerms):
			self.searchResultsList.hide()
			self.searchResultsLabel.show()
			self.searchResultsLabel.setText('Ready.')
			return
		try:
			if re.match(r'^\d+$', searchTerms): # It's an author ID search
				sqlResult = sqlQuery('SELECT * FROM `authors` WHERE `auid` = ' + searchTerms + ' LIMIT 1', asDict=True).fetchall()
			else: # It's a name search
				conditions = ["`name` REGEXP '" + x.replace('\\', '\\\\').replace('\'', '\\\'') + "'" for x in searchTerms.split(' ')]
				sqlResult = sqlQuery('SELECT * FROM `authors` WHERE ' + ' AND '.join(conditions), asDict=True).fetchall()
		except Exception, e:
			self.status.setText(unicode(e))
			return
		if not len(sqlResult):
			self.searchResultsList.hide()
			self.searchResultsLabel.show()
			self.searchResultsLabel.setText('No authors found!')
			return
		self.authors = authorsTable.fromResults(sqlResult)
		self.searchResultsList.clear()
		for a in self.authors:
			self.searchResultsList.addItem(a['name'])
		self.searchResultsLabel.hide()
		self.searchResultsList.show()
		self.searchResultsList.setCurrentRow(0)
	def changeAuthor(self):
		self.itemsList.clear()
		self.status.setText('')
		author = self.authors[self.searchResultsList.currentRow()]
		try:
			query = sqlQuery("""
				      SELECT items.iid, title, date, 'Video'    AS type FROM items NATURAL JOIN authored_by NATURAL JOIN video     WHERE `auid` = %auid%
				UNION SELECT items.iid, title, date, 'Audio'    AS type FROM items NATURAL JOIN authored_by NATURAL JOIN audio     WHERE `auid` = %auid%
				UNION SELECT items.iid, title, date, 'Book'     AS type FROM items NATURAL JOIN authored_by NATURAL JOIN books     WHERE `auid` = %auid%
				UNION SELECT items.iid, title, date, 'Magazine' AS type FROM items NATURAL JOIN authored_by NATURAL JOIN magazines WHERE `auid` = %auid%
			""".replace('%auid%', str(author['auid'])), asDict=True).fetchall()
		except Exception, e:
			self.itemsLabel.show()
			self.itemsList.hide()
			self.status.setText(unicode(e))
			return
		if not len(query):
			self.itemsLabel.show()
			self.itemsList.hide()
			self.itemsLabel.setText('No items found!')
		self.itemsLabel.hide()
		self.itemsList.show()
		for r in query:
			self.itemsList.addTopLevelItem(QtGui.QTreeWidgetItem([r['title'], r['type'], unicode(r['date'])]))

if __name__ == '__main__':
	runApp(4)
