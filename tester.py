#overwatch data retriever
#utilizes both the python-overwatch api and beautiful soup to retrive data
from bs4 import BeautifulSoup
from overwatch import Overwatch
import pyodbc


def getInfo(heroName, ow):
    data = []
    game = ow(mode="cp", hero=heroName, filter="game")
    i = game.index('Time Played')
    data.append(game[i+1])
    combat = ow(mode="cp", hero=heroName, filter="combat")
    i = combat.index('All Damage Done')
    data.append(combat[i+1])
    i = combat.index('Deaths')
    data.append(combat[i+1])
    i = combat.index('Eliminations')
    data.append(combat[i+1])
    i = combat.index('Objective Kills')
    data.append(combat[i+1])
    i = combat.index('Objective Time')
    data.append(combat[i+1])
    assists = ow(mode="cp", hero=heroName, filter="assists")
    i = assists.index('Healing Done')
    data.append(assists[i+1])
    return data

def main():
    overwatch = Overwatch(battletag="Serb#11472")
    print(getInfo('Lucio', overwatch))
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
if __name__ == '__main__':
    main()
