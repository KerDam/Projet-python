from Installation import Installation
from Activite import Activite
from Equipement import Equipement
import csv

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
