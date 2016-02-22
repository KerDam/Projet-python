class Activite :

	def __init__(self, com_insee, com_nom, eq_num, nb_eq_id, act_code, act_lib, act_prat) :
		""" Constructeur de la classe Activite
			Param1: Code INSEE de la commune
			Param2: Nom de la commune
			Param3: Numéro de la fiche équipement
			Param4: Nombre d'équipements identiques
			Param5: Code de l'activité
			Param6: Libellé de l'activité
			Param7: Activité pratiquée
		"""
		self.com_insee = com_insee
		self.com_nom = com_nom
		self.eq_num = eq_num
		self.nb_eq_id = nb_eq_id
		self.act_code = act_code
		self.act_lib = act_lib
		self.act_prat = act_prat

	def __str__(self) :
		""" Permet de représenter une Activité """
		return "Code INSEE de la commune : " + self.com_insee + " , Nom de la commune : " + self.com_nom + " , Numéro de la fiche équipement : " + self.eq_num + " , Nombre d'équipements identiques : " + self.nb_eq_id + " , Code de l'activité : " + self.act_code + " , Libellé de l'activité : " + self.act_lib + " , Activité pratiquée : " + self.act_prat

# ---------- GETTERS ----------------

	def get_com_insee(self) :
		return self.com_insee

	def get_com_nom(self) :
		return self.com_nom

	def get_eq_num(self) :
		return self.eq_num

	def get_nb_eq_id(self) :
		return self.nb_eq_id

	def get_act_code(self) :
		return self.act_code

	def get_act_lib(self) :
		return self.act_lib

	def get_act_prat(self) :
		return self.act_prat

# -----------------------------------
