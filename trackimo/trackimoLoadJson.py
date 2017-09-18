import sqlite3
import json
import codecs

conn = sqlite3.connect('dbtrackimo.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM track WHERE duracion > 30 ORDER BY fecha, duracion desc')
fhand = codecs.open('where.js', 'w', "utf-8")
fhand.write("myData = [\n")
count = 0
for row in cur :
    lat = row[1]
    lng = row[2]
    if lat == 0 or lng == 0 : continue
    where = row[0] + '-' + str(row[3])
    try :
        print(where, lat, lng)
        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open viewLocations.html to view the data in a browser")

