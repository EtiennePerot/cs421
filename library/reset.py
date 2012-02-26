from base import *
from authors import *
from genres import *
from items import *
from languages import *
from publishers import *
from people import *
from actors import *

def reset():
	tableOrder = [
		itemsTable, booksTable, videoTable, audioTable, songsTable, magazinesTable,
		peopleTable, employeesTable, membersTable,
		genresTable, authorsTable, publishersTable, languagesTable, actorsTable, instancesTable,
		authoredByTable, publishedByTable, hasLanguagesTable, hasActorsTable, reservedByTable
	]
	# First, drop in reverse order
	for table in reversed(tableOrder):
		table.drop()
	# Then recreate in normal order
	for table in tableOrder:
		table.create()

if __name__ == '__main__':
	if raw_input('Are you sure you want to reset everything? (Y/n) ').lower() in ('y', 'yes', ''):
		reset()
