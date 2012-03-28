from PySide import QtCore, QtGui
from p4_q2_ui import *
from library import *
import re

class MultiEditorLine(QtGui.QHBoxLayout):
	def __init__(self, editor, index):
		QtGui.QHBoxLayout.__init__(self)
		self._editor = editor
		self._label = QtGui.QLabel(editor._label + ' ' + str(index + 1) + ': ')
		self.addWidget(self._label, 1, QtCore.Qt.AlignRight)
		innerLayout = QtGui.QHBoxLayout()
		self.addLayout(innerLayout, editor._columnRatio)
		self._widget = editor.buildWidget()
		innerLayout.addWidget(self._widget, 1)
		self._button = QtGui.QPushButton('-')
		self._button.clicked.connect(self.remove)
		innerLayout.addWidget(self._button, 0)
	def setIndex(self, index):
		self._label.setText(self._editor._label + ' ' + str(index + 1) + ': ')
	def remove(self):
		self._label.deleteLater()
		self._button.deleteLater()
		self._widget.deleteLater()
		self._editor.remove(self)

class MultiEditor(QtGui.QVBoxLayout):
	def __init__(self, label, widget, func=None, columnRatio=1):
		QtGui.QVBoxLayout.__init__(self)
		self._label = label
		self._widget = widget
		self._func = func
		self._columnRatio = columnRatio
		self._items = []
		addLayout = QtGui.QHBoxLayout()
		addLayout.addStretch(1)
		addBox = QtGui.QHBoxLayout()
		addButton = QtGui.QPushButton('+')
		addButton.clicked.connect(self.add)
		addBox.addWidget(addButton, 0)
		addBox.addWidget(QtGui.QLabel('Add ' + label.lower()), 1)
		addLayout.addLayout(addBox, self._columnRatio)
		self.addLayout(addLayout)
		self.add()
	def buildWidget(self):
		widget = self._widget()
		if self._func is not None:
			self._func(widget)
		return widget
	def add(self):
		line = MultiEditorLine(self, len(self._items))
		self._items.append(line)
		self.insertLayout(len(self._items) - 1, line)
	def remove(self, item):
		index = self._items.index(item)
		self.takeAt(index).layout().deleteLater()
		del self._items[index]
		for i, l in enumerate(self._items):
			l.setIndex(i)
	def __iter__(self):
		for i in self._items:
			yield i._widget

class LanguageMenu(QtGui.QComboBox):
	def __init__(self):
		QtGui.QComboBox.__init__(self)
		for l in languageData:
			self.addItem(l['english'] + u' (' + l['translated'] + u')', l['iso'])
		self.setMinimumWidth(150)
	def getLanguage(self):
		return self.itemData(self.currentIndex())


class Option1(UIOption):
	def __init__(self):
		self._columnRatio = 4
		UIOption.__init__(self, True)
	def getTitle(self):
		return 'Add a book'
	def makeField(self, label, widget):
		l = QtGui.QHBoxLayout()
		if label is None:
			l.addStretch(1)
		else:
			l.addWidget(QtGui.QLabel(label + ': '), 1, QtCore.Qt.AlignRight)
		if isinstance(widget, QtGui.QLayout):
			l.addLayout(widget, self._columnRatio)
		else:
			l.addWidget(widget, self._columnRatio)
		self._layout.addLayout(l)
	def initUI(self, layout):
		self.label = QtGui.QLabel('Adding a new book')
		layout.addWidget(self.label)
		self.title = QtGui.QLineEdit()
		self.title.setPlaceholderText('Book title...')
		self.makeField('Title', self.title)
		self.date = QtGui.QDateEdit(QtCore.QDate.currentDate())
		self.makeField('Date', self.date)
		self.isbn = QtGui.QLineEdit()
		self.isbn.setPlaceholderText('Book ISBN...')
		self.makeField('ISBN', self.isbn)
		self.pages = QtGui.QSpinBox()
		self.pages.setMinimum(2)
		self.pages.setSuffix(' pages')
		self.makeField('Pages', self.pages)
		self.genres = MultiEditor('Genre', QtGui.QLineEdit, lambda x : x.setPlaceholderText('Genre name...'), columnRatio=self._columnRatio)
		layout.addLayout(self.genres)
		self.languages = MultiEditor('Language', LanguageMenu, columnRatio=self._columnRatio)
		layout.addLayout(self.languages)
		self.authors = MultiEditor('Author', QtGui.QLineEdit, lambda x : x.setPlaceholderText('Author name...'), columnRatio=self._columnRatio)
		layout.addLayout(self.authors)
		self.publishers = MultiEditor('Publisher', QtGui.QLineEdit, lambda x : x.setPlaceholderText('Publisher name...'), columnRatio=self._columnRatio)
		layout.addLayout(self.publishers)
		statusBar = QtGui.QHBoxLayout()
		self.statusLabel = QtGui.QLabel('')
		statusBar.addWidget(self.statusLabel, 0, QtCore.Qt.AlignCenter)
		layout.addLayout(statusBar)
		self.addButton = QtGui.QPushButton('Add book')
		self.addButton.clicked.connect(self.add)
		addBar = QtGui.QHBoxLayout()
		addBar.addWidget(self.addButton, 0, QtCore.Qt.AlignCenter)
		layout.addLayout(addBar)
	def add(self):
		try:
			if not self.title.text():
				raise Exception('Title field is empty.')
			if not re.match(r'\d+', self.isbn.text()):
				raise Exception('ISBN is not valid.')
			nonEmpty = lambda x : x.text()
			languages = [t.getLanguage() for t in self.languages]
			authors = [authorByName(t.text()) or Author.create(name=t.text()) for t in filter(nonEmpty, self.authors)]
			if not authors:
				raise Exception('Must specify at least one author.')
			publishers = [publisherByName(t.text()) or Publisher.create(name=t.text()) for t in filter(nonEmpty, self.publishers)]
			if not publishers:
				raise Exception('Must specify at least one publisher.')
			genres = [t.text() for t in filter(nonEmpty, self.genres)]
			if not genres:
				raise Exception('Must specify at least one genre.')
			# All good, ready to submit.
			transactionStart()
			Book.create(
				title=self.title.text(),
				date=self.date.date().toString('yyyy-MM-dd'),
				isbn=int(self.isbn.text()),
				pages=self.pages.value(),
				genres=genres,
				authors=authors,
				publishers=publishers,
				languages=languages
			)
			transactionCommit()
			self.statusLabel.setText('Book added!')
		except Exception, e:
			self.statusLabel.setText(str(e))

if __name__ == '__main__':
	runApp(0)
