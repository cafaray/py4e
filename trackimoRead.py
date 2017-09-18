import sqlite3
import json
import time

fname = input('Enter the filename:')
if len(fname)<=0:
    print('assigning automatic name to export.csv')
    fname = 'export.csv'

try:
    fhandle = open(fname)
except:
    print('bad filename, exiting')
    quit()

print('starting process ...')

connection = sqlite3.connect('dbtrackimo.sqlite')
cur = connection.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS track (fecha text, latitud real, longitud real, duracion integer, url text); ''')
cur.execute('''DELETE FROM track;''')
connection.commit()
print('database created ...')
count = 0
for line in fhandle:
    # print('line: ',count,line)
    parts = line.split(',')
    if len(parts) < 6:
        continue
    date = parts[0].replace('"','')
    lat = parts[1]
    lng = parts[2]
    duration = parts[3]
    url = parts[4] + ',' + parts[5]
    url = url.replace('"','')
    fechaHora = date.split()
    fecha = fechaHora[0].split('/')
    hora = fechaHora[1]
    strFecha = '20' + fecha[2]+ '-' + fecha[1] + '-' + fecha[0]
    sqliteFecha = date.split('/')
    print('    ==> date: ',date,'     url:',url)
    cur.execute('''INSERT INTO track (fecha, latitud, longitud, duracion, url) VALUES (?, ?, ?, ?, ?)''', (strFecha + ' ' + hora,lat,lng,duration,url))
    connection.commit()

print('end of process')
