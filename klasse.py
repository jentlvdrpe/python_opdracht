class Vriend:
	def __init__(self, last_name, first_name, country):
		self.achternaam = last_name.title()
		self.voornaam = first_name.title()
		self.land = country.title()

	def geef_land(self):
		return self.land

	def geef_naam(self):
		naam = self.achternaam + " " + self.voornaam
		return naam