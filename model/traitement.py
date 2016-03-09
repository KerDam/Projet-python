from Dao import Dao

class Traitement(object):

	def __init__(self):
		self.dao = Dao("E146084M", "E146084M", "E146084M")

	def getActivites(self):
		return self.dao.select("select distinct ActCode, ActLib from activites")

	def getVilles(self):
		return self.dao.select("select distinct `Code INSEE`, `Nom de la commune` from installations")

