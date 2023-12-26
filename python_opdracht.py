import sqlite3, sys, csv
from klasse import Vriend 

# Definieer je drie argumenten
script, achternaam, voornaam, land, database = sys.argv

# Maak een klasse aan
vriend = Vriend(achternaam, voornaam, land)

# Openen van de database
try:
	dbconnectie = sqlite3.connect(database)
	cursor = dbconnectie.cursor()
except Exception as e:
	print("Fout bij het openen database: ", e)
	sys.exit(1)

# Print de originele database
print("Originele database:")
cursor.execute("SELECT * FROM friends")
for friend in cursor:
	print(friend)

# Pas de database aan
cursor.execute('UPDATE friends SET country=? WHERE first_name=?', (vriend.land, vriend.voornaam))
dbconnectie.commit()

# Print de originele database met de aanpassing
print("\nAangepaste database:")
cursor.execute("SELECT * FROM friends")
for friend in cursor:
	print(friend)

cursor.close()
dbconnectie.close()

# Inlezen van een csv-bestand
'''try:
	with open('friends.csv', 'w', newline='') as friends_bestand:
		writer = csv.writer(friends_bestand)
		writer.writerow(['name', 'age'])
except Exception as e:
	print("Fout bij wegschrijven: ", e)
	sys.exit(1)'''