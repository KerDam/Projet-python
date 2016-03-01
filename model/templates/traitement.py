from Dao import Dao
class traitement(object):

	def __init__(self):
		dao = Dao("E146084M","E146084M", "E146084M")

	def getActivite(self):
		cursor = self.dao.select("select ComLib from activites")

