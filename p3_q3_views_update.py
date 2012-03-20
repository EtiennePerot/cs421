from library import sqlQuery

#This file assumes the views have already been created

print sqlQuery("""
UPDATE CurrentReserves SET title = '????' WHERE 200 < iid AND iid < 400
""")
