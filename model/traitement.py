from Dao import Dao

class traitement(object):

	def __init__(self):
		self.dao = Dao("E146084M", "E146084M", "E146084M")

	def getActivites(self):
		return self.dao.select("select ComLib from activites")

	def getVilles(self):
		return self.dao.select("select `Nom de la commune` from installations")

