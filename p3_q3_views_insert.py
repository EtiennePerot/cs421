from library import sqlQuery

# This file assumes the views have already been created

print sqlQuery("""
INSERT INTO CurrentReserves(iid, instid, title, pnid) values(900, 200, 'Wuthering Heights', 999)
""")

print sqlQuery("""
INSERT INTO OnlyOneInstance(iid, title) values(669, ‘Sunset Boulevard’)
""")
