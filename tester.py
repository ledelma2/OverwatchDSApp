#overwatch data retriever
#utilizes both the python-overwatch api and beautiful soup to retrive data
from bs4 import BeautifulSoup
from overwatch import Overwatch
import pyodbc


overwatch = Overwatch(battletag="Serb#11472")
print(overwatch(mode="cp", hero="ana", filter="game"))
db_file = r'''C:\Users\Liam Edelman\Documents\Personal\OverwatchDSApp\DB.accdb'''
user = 'admin'
password = ''
odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;UID=%s;PWD=%s' %\
                (db_file, user, password)
print('connecting to db...')
conn = pyodbc.connect(odbc_conn_str)
crsr = conn.cursor()
for table_info in crsr.tables():
    print(table_info.table_name)
print('closing db...')
conn.close()
