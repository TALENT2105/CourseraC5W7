#With this code we clean and structure data
#We create the tables States and Owners and Poverty

import sqlite3
import math

print('START')
SelectYear = 2013

# SelectYear=[]
# while SelectYear not in [2013, 2014, 2015, 2016] :
#     SelectYear = int(input('Enter year for the study (2013/2014/2015/2016):'))

ConnIn = sqlite3.connect('US_DATA.sqlite')
CurIn = ConnIn.cursor()
CurIn.execute('SELECT DISTINCT state FROM UsOwner ORDER BY state')

ConnOut = sqlite3.connect('US_DATA_CLEAN.sqlite')
CurOut = ConnOut.cursor()
CurOut.execute('CREATE TABLE IF NOT EXISTS State (id INTEGER UNIQUE, state TEXT)')

#Building the id<->state correspondance table called State
count = 0
for row in CurIn:
    count = count+1
    ConnOut.execute('INSERT OR IGNORE INTO State (id, state) VALUES (?,?)', (count, row[0]))
ConnOut.commit()

#Building the state_id/owner_rate table called Owner
CurOut.execute('CREATE TABLE IF NOT EXISTS Owner (state_id INTEGER UNIQUE, owner_rate REAL)')
CurIn.execute('SELECT state, owner FROM UsOwner WHERE year=? ORDER BY state', (SelectYear,))
for row in CurIn:
    CurOut.execute('SELECT id FROM State WHERE state=?', (row[0],))
    StId = CurOut.fetchone()[0]
    CurOut.execute('INSERT OR IGNORE INTO Owner (state_id, owner_rate) VALUES (?,?)', (StId, math.ceil(row[1]*100)/100))
ConnOut.commit()

#Building the state_id/poverty_rate table called Poverty
CurOut.execute('CREATE TABLE IF NOT EXISTS Poverty (state_id INTEGER UNIQUE, poverty_rate REAL)')
CurIn.execute('SELECT state, percentage FROM UsPoverty WHERE year=? ORDER BY state', (SelectYear,))
for row in CurIn:
    CurOut.execute('SELECT id FROM State WHERE state=?', (row[0],))
    StId = CurOut.fetchone()[0]
    CurOut.execute('INSERT OR IGNORE INTO Poverty (state_id, poverty_rate) VALUES (?,?)', (StId, math.ceil(row[1]*100)/100))
ConnOut.commit()

CurIn.close()
CurOut.close()
print('END')

