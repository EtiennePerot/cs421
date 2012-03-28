from PySide import QtCore, QtGui
from p4_q2_ui import *
from library import *
import re, datetime

class MagazineRow(object):
	def __init__(self, index, table, item, magazine):
		self.index = index
		self.item = item
		self.magazine = magazine
		self.iid = self.item['iid']
		self.titleField = QtGui.QTableWidgetItem(self.item['title'])
		self.dateField = QtGui.QTableWidgetItem(unicode(self.item['date']))
		self.issnField = QtGui.QTableWidgetItem(unicode(self.magazine['issn']))
		self.issueField = QtGui.QTableWidgetItem(unicode(self.magazine['issue']))
		self.pagesField = QtGui.QTableWidgetItem(unicode(self.magazine['pages']))
		self.cells = [
			(self.titleField, r'.+',                 self.item,     'title', unicode),
			(self.dateField,  r'\d\d\d\d-\d\d-\d\d', self.item,     'date',  self.getDate),
			(self.issnField,  r'\d+',                self.magazine, 'issn',  int),
			(self.issueField, r'\d+',                self.magazine, 'issue', int),
			(self.pagesField, r'\d+',                self.magazine, 'pages', int)
		]
		self.table = table
		for i, c in enumerate(self.cells):
			self.table.setItem(self.index, i, c[0])
	def getDate(self, date):
		return datetime.date(*map(int, date.split('-')))
	def revert(self, c):
		pass
	def update(self):
		for c in self.cells:
			if not re.match(c[1], c[0].text()):
				self.revert(c)
			try:
				t = c[4](c[0].text())
			except:
				self.revert(c)
				continue
			if c[2][c[3]] == c[0].text():
				continue
				continue
			c[2][c[3]] = t
		self.item.sync()
		self.magazine.sync()

class Option3(UIOption):
	def __init__(self):
		UIOption.__init__(self)
	def getTitle(self):
		return 'Magazines editor'
	def initUI(self, layout):
		columns = ('Title', 'Date', 'ISSN', 'Issue', 'Pages')
		layout.addWidget(QtGui.QLabel('The following table contains a list of magazines\nIt can be interactively edited by double-clicking on a cell.'))
		magResults = sqlQuery("""SELECT * FROM items NATURAL JOIN magazines""", asDict=True).fetchall()
		allItems = itemsTable.fromResults(magResults)
		allMagazines = magazinesTable.fromResults(magResults)
		self.table = QtGui.QTableWidget(len(magResults), len(columns))
		self.table.setHorizontalHeaderLabels(columns)
		self.rows = [MagazineRow(i, self.table, allItems[i], allMagazines[i]) for i in xrange(len(allItems))]
		layout.addWidget(self.table)
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.updateDatabase)
		self.timer.start(1000)
	def updateDatabase(self):
		for r in self.rows:
			r.update()

if __name__ == '__main__':
	runApp(2)
