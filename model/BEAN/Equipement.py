class Equipement:

	def __init__(self, com_insee, com_nom, ins_num, ins_nom, eq_num, eq_nom, bat_nom, eq_type) :
		""" Constructeur de la classe Equipement
			Param1: Code INSEE de la commune
			Param2: Nom de la commune
			Param3:	Numéro de l'installation
			Param4: Nom de l'installation
			Param5: Numéro de la fiche équipement
			Param6: Nom de la fiche équipement
			Param7: Nom du batiment
			Param8: Type de l'équipement
		"""
		self.com_insee = com_insee
		self.com_nom = com_nom
		self.ins_num = ins_num
		self.ins_nom = ins_nom
		self.eq_num = eq_num
		self.eq_nom = eq_nom
		self.bat_nom = bat_nom
		self.eq_type = eq_type

	def __str__(self) :
		""" Permet de représenter un Equipement """
		return "Code INSEE de la commune : " + self.com_insee + " , Nom de la commune : " + self.com_nom + " , Numéro de l'installation : " + self.ins_num + " , Nom de l'installation : " + self.com_nom + " , Numéro de la fiche équipement : " + self.eq_num + " , Nom de la fiche équipement : " + self.eq_nom + " , Nom du batiment : " + self.bat_nom + " , Type de l'équiement : " + self.eq_type
	
# ----------- GETTERS ---------------

	def get_com_insee(self) :
		return self.com_insee

	def get_com_nom(self) :
		return self.com_nom

	def get_ins_num(self) :
		return self.ins_num

	def get_ins_nom(self) :
		return self.ins_nom

	def get_eq_num(self) :
		return self.eq_num

	def get_eq_nom(self) :
		return self.eq_nom

	def get_bat_nom(self) :
		return self.bat_nom	

	def get_eq_type(self) :
		return self.eq_type

# ------------------------------------