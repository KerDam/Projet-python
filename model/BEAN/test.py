from CreateFromCSV import CreateFromCSV
from Installation import Installation
from Activite import Activite
from Equipement import Equipement

csv = CreateFromCSV('../../donnees/activites.csv')
retour = csv.create()
for r in retour :
	print(r)