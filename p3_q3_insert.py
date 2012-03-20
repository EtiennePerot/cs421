from library import sqlQuery

print sqlQuery("""INSERT INTO CurrentReserves(iid, instid, title, pnid) values(900, 200, 'Wuthering Heights', 999);
INSERT INTO OnlyOneInstance(iid, title) values(669, ‘Sunset Boulevard’);
""")
