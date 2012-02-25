from base import *

itemsTable = _dbTable('items', '*iid', 'title', 'date')
Item = itemsTable.genClass()

booksTable = _dbTable('books', '*iid', 'isbn', 'pages')
Book = booksTable.genClass()
