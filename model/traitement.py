from Dao import Dao

class Traitement(object):

	def __init__(self):
		self.dao = Dao("E146084M", "E146084M", "E146084M")

	def getActivites(self):
		return self.dao.select("select distinct ActCode, ActLib from activites order by ActLib")

	def getVilles(self):
		return self.dao.select("select distinct `Code INSEE`, `Nom de la commune` from installations order by `Nom de la commune`")

	def getInstallations(self, actcode, insee):
		return 	

