from Dao import Dao

class Traitement(object):

	def __init__(self):
		self.dao = Dao("E146084M", "E146084M", "E146084M")

	def getActivites(self):
		return self.dao.select("select distinct ActCode, ActLib from activites order by ActLib")

	def getVilles(self):
		return self.dao.select("select distinct `Code INSEE`, `Nom de la commune` from installations order by `Nom de la commune`")

	def getInstallations(self, actcode, insee):
		installations = [["3","rue maréchal joffre", "44000", "nantes", "47.2230865", "-1.546768"],["1","rue je sais pas", "44000", "carquefou", "47.2823186", "-1.5227437"]]
		return 	installations

