import sqlite3, sys, csv
from klasse import Vriend 

# Definieer je drie argumenten
#script, inputbestand, database, output = sys.argv

vriend = Vriend("Kouwenhoven", "Tim", "Belgium")

query = """

"""

# Openen van de database
try:
	dbconnectie = sqlite3.connect("friends.db")
	cursor = dbconnectie.cursor()
except Exception as e:
	print("Fout bij het openen database: ", e)
	sys.exit(1)



# Inlezen van een csv-bestand
try:
	with open('friends.csv', 'w', newline='') as friends_bestand:
		writer = csv.writer(friends_bestand)
		writer.writerow(['name', 'age'])
except Exception as e:
	print("Fout bij wegschrijven: ", e)
	sys.exit(1)