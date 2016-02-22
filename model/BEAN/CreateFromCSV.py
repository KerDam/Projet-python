import csv
from Data import Data

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

    @staticmethod
    def addDataBase(self,data):
        array = CreateFromCSV.create(data)
        for dic in array:
            request = "Insert into" + data.getNomTable() + "values ("
            for value in dic.values():
                request += value
            print request
