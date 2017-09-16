import sqlite3

conn = sqlite3.connect('ejercicio15.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Counts''')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
print('opening file',fname)
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    mail = pieces[1]
    print('looking in string mail:',mail)
    iniPosition = mail.find('@')
    #endPosition = mail.find('.', iniPosition)
    org = mail[iniPosition+1: ] #endPosition]
    print('looking for org:',org)
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
