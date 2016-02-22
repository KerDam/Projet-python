class Data :

	def __init__(self, fichier, nomTable, attributs) :

		self.fichier = fichier
		self.nomTable = nomTable
		self.attributs = attributs


	def getFichier() :
		return self.fichier

	def getNomTable() :
		return self.nomTable

	def getAttributs() :
		return self.attributs