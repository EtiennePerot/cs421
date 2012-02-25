from base import *

authorsTable = dbTable('authors', '*auid', 'name')
Author = authorsTable.genClass()

def authorByName(name):
	return authorsTable.findSingle(name=name)

authoredByTable = dbTable('authored_by', '*iid', '*auid')
AuthoredBy = authoredByTable.genClass()

if __name__ == '__main__':
	#Author.create(name='Cory Doctorow')
	#Author.create(name='Albert Camus')
	#Author.create(name='Victor Hugo')
	#Author.create(name='Samuel Beckett')
	#Author.create(name='Balzac')
	print byName('Albert Camus')
