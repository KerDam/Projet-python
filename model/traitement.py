from Dao import Dao

class traitement(object):

	def __init__(self):
		# self.dao = Dao("E146084M", "E146084M", "E146084M")
		self.dao = Dao("django", "django", "django")


	def getActivites(self):
		return self.dao.select("select distinct ActLib, ActCode from activites order by ActLib")
		# for i in array:
			# print (i)

	def getVilles(self):
		return self.dao.select("select distinct `Nom de la commune` from installations order by `Nom de la commune`")
		# for i in array:
			# print (i)
	def getActiviteVille(self, activite, ville):
            return self.dao.select("select `Numero de la voie`,`Nom de la voie`, `Code postal`, `Nom de la commune` from installations, (select InsNumeroInstall from equipements where equipements.EquipementId in (select EquipementId from activites where ActCode = 2901 and ComInsee = 44001)) equ where installations.`Numéro de l installation` = equ.InsNumeroInstal")
