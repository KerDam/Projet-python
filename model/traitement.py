from Dao import Dao

class Traitement(object):

	def __init__(self):
		# self.dao = Dao("E146084M", "E146084M", "E146084M")
		self.dao = Dao("django", "django", "django")


	def getActivites(self):
<<<<<<< HEAD
		return self.dao.select("select distinct ActLib, ActCode from activites order by ActLib")
		# for i in array:
			# print (i)

	def getVilles(self):
		return self.dao.select("select distinct `Nom de la commune` from installations order by `Nom de la commune`")
		# for i in array:
			# print (i)
	def getActiviteVille(self, activite, ville):
            return self.dao.select("select `Numero de la voie`,`Nom de la voie`, `Code postal`, `Nom de la commune` from installations, (select InsNumeroInstall from equipements where equipements.EquipementId in (select EquipementId from activites where ActCode = 2901 and ComInsee = 44001)) equ where installations.`Numéro de l installation` = equ.InsNumeroInstal")
=======
		return self.dao.select("select distinct ActCode, ActLib from activites order by ActLib")

	def getVilles(self):
		return self.dao.select("select distinct `Code INSEE`, `Nom de la commune` from installations order by `Nom de la commune`")

	def getInstallations(self, actcode, insee):
		installations = [["3","rue maréchal joffre", "44000", "nantes", "47.2230865", "-1.546768"],["1","rue je sais pas", "44000", "carquefou", "47.2823186", "-1.5227437"]]
		return 	installations

>>>>>>> ee46ef855b23dbd4ddbb1a691ee2ffb78c667077
