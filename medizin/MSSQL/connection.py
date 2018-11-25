import pyodbc


con = pyodbc.connect('Trusted_Connection=yes', driver = '{ODBC Driver 13 for SQL Server}',server = 'localhost', database = 'MediZine',UID='sa',PWD='enter')



cursor = con.cursor()
cursor.execute('select * from ID_GNTR')

for row in cursor:
    print('row = %r' % (row,))