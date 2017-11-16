from sqlalchemy import Table, Column, Integer, String, ForeignKey
from ap import connect

con, meta = connect('postgres', 'postgres', 'dbtest')
slams = Table('slams', meta,
    Column('name', String, primary_key=True),
    Column('country', String)
)

results = Table('results', meta,
    Column('slam', String, ForeignKey('slams.name')),
    Column('year', Integer),
    Column('result', String)
)

# Create the above tables

print con
meta.create_all(con)
# for table in meta.tables:
#     print table