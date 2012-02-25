from base import *

genresTable = dbTable('genres', '*iid', 'name')
Genre = genresTable.genClass()

# No sample data here; things are created along with items
