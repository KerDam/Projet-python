from Dao import Dao

class Traitement(object):

	def __init__(self):
		# self.dao = Dao("E146084M", "E146084M", "E146084M")
		self.dao = Dao("django", "django", "django")


	def getActivites(self):
		""" Récupère toutes les activités de la base de données """
		return self.dao.select("select distinct ActLib, ActCode from activites order by ActLib")
		# for i in array:
			# print (i)


	def getInstallations(self, activite, ville):
		""" Récupère toutes les installations 
		où l'on peut pratiquer l'activité passée en paramètre 
		dans la ville passée en paramètre """
            return self.dao.select("select `Nom usuel de l installation`, `Numero de la voie`,`Nom de la voie`, `Code postal`, `Nom de la commune`, EquGpsX , EquGpsY from installations, (select InsNumeroInstall , EquGpsX, EquGpsY from equipements where equipements.EquipementId in (select EquipementId from activites where ActCode = "+activite+" and ComInsee = "+ville+"))  equ where installations.`Numéro de l installation` = equ.InsNumeroInstall")


	def getVilles(self):
		""" Récupère toutes les villes de la base de données """
		return self.dao.select("select distinct `Code INSEE`, `Nom de la commune` from installations order by `Nom de la commune`")
