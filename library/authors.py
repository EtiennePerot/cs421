from base import *

table = _dbTable('authors', '*auid', 'name')
Author = table.genClass()
