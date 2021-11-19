import sqlite3

connection = sqlite3.connect('emaildb.sqlite')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS Counts')

cursor.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fName = input("Enter file name - ")
if len(fName) < 1:
    fName = 'mbox.txt'

try:
    fHand = open(fName)
except:
    print('Cannot open file')
    quit()

iterations = 0
for line in fHand:
    if line.startswith("From: "):

        # splits the text into just the org's domain name
        pieces = line.split()
        email = pieces[1]
        org = email.split("@")[1]
        
        # selects count of organization
        cursor.execute('''
        SELECT count FROM Counts WHERE org = ?
        ''', (org, ))
        row = cursor.fetchone()

        # sets the count to 1 if the row is not there, or adds 1 to it if it is
        if row is None:
            cursor.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org, ))
        else:
            cursor.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org, ))

        # commits the changes to the database
        if iterations == 10:
            connection.commit()
            iterations = 0
        else:
            iterations += 1
    else:
        continue

connection.commit()

sqlstr = 'SELECT org,count FROM Counts ORDER BY count DESC'

for row in cursor.execute(sqlstr):
    print(str(row[0]), row[1])

cursor.close()