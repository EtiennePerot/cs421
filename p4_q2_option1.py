from PySide import QtCore, QtGui
from p4_q2_ui import *
from library import *

class Option1(UIOption):
	def __init__(self):
		UIOption.__init__(self)
	def getTitle(self):
		return 'Audio albums'
	def initUI(self, layout):
		self.label = QtGui.QLabel('Loading...')
		layout.addWidget(self.label)
		try:
			qry = sqlQuery("""SELECT title, date, format, albumSongs.numSongs, ROUND(albumSongs.totalAlbumDuration / 60) AS totalDuration
				FROM items NATURAL JOIN audio NATURAL JOIN (
					SELECT audio.iid, COUNT(track) AS numSongs, SUM(songs.duration) AS totalAlbumDuration
					FROM audio NATURAL JOIN songs
					GROUP BY audio.iid
				) AS albumSongs""")
			results = qry.fetchall()
		except Exception, e:
			self.label.setText('Error: ' + str(e))
			return
		if not len(results):
			self.label.setText('No results to display!')
			return
		self.label.setText('Displaying all albums in the database, along with number of tracks and total duration (aggregation).')
		self.table = QtGui.QTableWidget(len(results), len(results[0]))
		self.table.setHorizontalHeaderLabels(('Album title', 'Date', 'Format', 'Number of songs', 'Album duration'))
		itemFlags = QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled
		for r in xrange(len(results)):
			for c in xrange(len(results[r])):
				widget = QtGui.QTableWidgetItem(unicode(results[r][c]))
				widget.setFlags(itemFlags)
				self.table.setItem(r, c, widget)
		layout.addWidget(self.table)
