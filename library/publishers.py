from base import *

publishersTable = dbTable('publishers', '*pid', 'name')
Publisher = publishersTable.genClass()

def publisherByName(name):
	return publishersTable.findSingle(name=name)

publishedByTable = dbTable('published_by', '*iid', '*pid')
PublishedBy = publishedByTable.genClass()

if __name__ == '__main__':
	# Sample data
	Publisher.create(name='Hachette')
	Publisher.create(name='Freshbooks')
	Publisher.create(name='First Choice')
	Publisher.create(name='Room To Read')
	Publisher.create(name='Xlibris')
