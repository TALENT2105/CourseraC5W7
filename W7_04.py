#With this code we clean and structure data
#We create the tables States and Owners and Poverty

import sqlite3

print('START')
Conn = sqlite3.connect('US_DATA_CLEAN.sqlite')
Cur = Conn.cursor()

Cur.execute('SELECT COUNT(state_id) FROM Poverty')
num_line=Cur.fetchone()[0]

Cur.execute('''SELECT State.state, Poverty.poverty_rate, Owner.owner_rate 
FROM State 
JOIN Poverty JOIN Owner 
ON State.id=Poverty.state_id 
AND State.id=Owner.state_id
ORDER BY Owner.owner_rate''')

print('\nSTATE / POVERTY RATE / OWNER RATE\n')
print('------------------------------------------------------------------------')

fhand = open('W7_05.js','w')
fhand.write("scatter = [ ['Poverty Rate','Ownership Rate'],\n")
count=0
for row in Cur:
    count=count+1
    print(row[0],' / ',row[1],' / ', row[2])
    if count < num_line:
        fhand.write("["+str(row[1])+','+str(row[2])+'],\n')
    else:
        fhand.write("[" + str(row[1]) + ',' + str(row[2]) + ']')
fhand.write("\n];\n")
fhand.close()

Cur.close()
print('END')