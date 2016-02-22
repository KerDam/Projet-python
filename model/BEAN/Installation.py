
class Installation :
	
	def __init__(self, ins_nom, ins_num, com_nom, com_insee, com_postal, ins_adr) :
		""" Constructeur de la classe Installation
			Param1: Nom de l'installation
			Param2: Numéro de l'installation
			Param3: Nom de la commune
			Param4: Code INSEE de la commune
			Param5: Code postal de la commune
			Param6: Adresse de l'installation
		"""
		self.ins_nom = ins_nom
		self.ins_num = ins_num
		self.com_nom = com_nom
		self.com_insee=com_insee
		self.com_postal = com_postal
		self.ins_adr = ins_adr

	def __str__(self) :
		""" Permet de représenter une Installation """
		return "Nom de l'installation : " + self.ins_nom + " , Numéro de l'installation : " + self.ins_num + " , Nom de la commune : " + self.com_nom + " , Code INSEE de la commune : " + self.com_insee + " , Code postal de la commune : " + self.com_postal + " , Adresse de l'installation : " + self.ins_adr

# ------------------ GETTERS -------------------- 

	def get_ins_nom(self) :
		return self.ins_nom

	def get_ins_num(self) :
		return self.ins_num

	def get_com_nom(self) :
		return self.com_nom

	def get_com_insee(self) :
		return self.com_insee

	def get_com_postal(self) :
		return self.com_postal

	def get_com_adr(self) :
		return self.ins_adr

# ------------------------------------------------


