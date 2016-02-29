class Data :

	def __init__(self, fichier, nomTable, attributs) :

		self.fichier = fichier
		self.nomTable = nomTable
		self.attributs = attributs


	def getFichier(self) :
		return self.fichier

	def getNomTable(self) :
		return self.nomTable

	def getAttributs(self) :
		return self.attributs
