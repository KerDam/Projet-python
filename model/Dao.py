import mysql.connector as mysql

class Dao :

	def __init__(self, username, password, base) :
		""" Constructeur de la classe Dao """
		self.username = username
		self.password = password
		self.base = base
		self.connexion = None

	def connexionDb(self) :
		""" Permet de se connecter à la base de données """
		try :
			self.connexion = mysql.connect(user=self.username, password=self.password, host="localhost", database=self.base)
		except mysql.connector.Error as err :
  			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR :
  				print("Something is wrong with your user name or password")
  			elif err.errno == errorcode.ER_BAD_DB_ERROR :
  				print("Database does not exist")
  			else :
  				print(err)
  			cnx.close()

	def deconnexion(self) :
		""" Permet de se déconnecter de la base de données """
		self.connexion.close()

	def insert(self,request):
		if self.connexion == None:
			self.connexionDb()
		cursor = self.connexion.cursor()
		cursor.execute(request)

	def commit(self):
		self.connexion.commit()

	def select(self,request):
		if self.connexion == None:
			self.connexionDb()
		cursor = self.connexion.cursor()
		cursor.execute(request)
		return cursor.fetchall()
