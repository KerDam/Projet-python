import csv
from Data import Data

class CreateFromCSV:

    def __init__(self,db):
        self.db = db

    @staticmethod
    def create(data):
        dataFile = open(data.getFichier(), "r")
        parserDict = csv.DictReader(dataFile)
        result = []
        for row in parserDict:
            dic ={}
            for i in data.getAttributs():
                try:
                    dic[i] = row[i]
                except KeyError:
                    print ("La clé " + i + "n'existe pas")
            result.append(dic)
        return result

    def addDataBase(data):
        array = CreateFromCSV.create(data)
        for dic in array:
            request = "Insert into" + data.getNomTable() + "values ("
            for value in dic.values():
                request += value +", "
            request = request[:len(request)-2]
            request += ")"
            print (request + '\n')

    def createTables(data):
        request = "Create table " + data.getNomTable() + "("
        for i in data.getAttributs():
            request += i + "varchar(255),"
        request = request[:len(request)-1]
        request += ")"
        print (request)
