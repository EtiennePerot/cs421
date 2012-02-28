import sys
from base import *
from authors import *
from genres import *
from items import *
from books import *
from magazines import *
from audio import *
from video import *
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
		try:
			table.drop()
		except: # Table probably doesn't exist
			pass
	# Then recreate in normal order
	for table in tableOrder:
		table.create()

def insertSamples():
	populateSampleMagazines()
	populateSampleAudio()

def ifApprove(question, execute):
	if raw_input(question + ' (Y/n) ').lower() in ('y', 'yes', ''):
		execute()

if __name__ == '__main__':
	ifApprove('Are you sure you want to reset everything?', reset)
	ifApprove('Recreate language data?', createLanguageData)
	ifApprove('Insert audio/magazines samples?', insertSamples)
	ifApprove('Generate 1000 IMDB movies?', curry(generateRandomVideo, 1000))
	ifApprove('Generate over nine thousand members?', curry(generateRandomPeople, 9001, printInfo=False))
