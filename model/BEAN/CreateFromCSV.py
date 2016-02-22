from Installation import Installation
from Activite import Activite
from Equipement import Equipement
import csv

<<<<<<< HEAD
class CreateFromCSV:
    @staticmethod
    def create(self, data):
        dataFile = open(data.getFichier, "r")
        parserDict = csv.DictReader(dataFile)
        result = []
        for row in parserDict:
            dic ={}
            for i in data.getAttributs:
                try:
                    dic[i] = row[i]
                except KeyError:
                    print ("La clé " + i + "n'existe pas")
            result.append(dic)
        return result
=======
class CreateFromCSV :

	def __init__(self, file_path) :
		self.file_path = file_path

	def create(self) :
		with open(self.file_path,'r') as csvfile :
			spamreader = csv.reader(csvfile, delimiter = ',')
			
			if self.file_path.find("installations") >= 0 :
				installations = []
				for row in spamreader :
					insta = Installation(row[0], row[1], row[2], row[3], row[4], row[6] + " " + row[7])
					installations.append(insta)
				return installations

			if self.file_path.find("activites") >= 0 :
				activites = []
				for row in spamreader :
					act = Activite(row[0], row[1], row[2], row[3], row[4], row[5], row[7])
					activites.append(act)
				return activites

			if self.file_path.find("equipements") >= 0 :
				equipements = []
				for row in spamreader :
					eq = Equipement(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
					equipements.append(eq)
				return equipements


>>>>>>> d4d65982d876fb57e14b805074ecea0365d8b449
