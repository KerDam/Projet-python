import csv
from Data import Data
from Dao import Dao

class CreateFromCSV:

    def __init__(self):
        self.db = Dao ("E146084M", "E146084M", "E146084M")

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

    def addDataBase(self,data):
        array = CreateFromCSV.create(data)
        for dic in array:
            request = "Insert into " + data.getNomTable() + " values ("
            for value in dic.values():
                request += "\"" + value.replace("\"","") +"\", "
            request = request[:len(request)-2]
            request += ")"
            print (request)
            self.db.insert(request)
        self.db.commit()


    def createTables(self,data):
        request = "Create table " + data.getNomTable() + "("
        for attributs in data.getAttributs():
            request += "`" + attributs.replace("\'", " ") + "` varchar(255),"
        request = request[:len(request)-1]
        request += ")"
        print (request)
        self.db.insert(request)
        self.db.commit()
