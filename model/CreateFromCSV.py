import csv
from Data import Data
from Dao import Dao

class CreateFromCSV:

    def __init__(self):
        """ Connexion à la base de données """
        # self.db = Dao ("E146084M", "E146084M", "E146084M")
       self.db = Dao ("django", "django","django")

    @staticmethod
    def create(data):
        """ Permet de récupérer toutes les données souhaitées à partir d'un fichier csv
        Cette méthode est appelée dans la méthode addDataBase
        param : un objet Data """
        dataFile = open(data.getFichier(), "r")
        parserDict = csv.DictReader(dataFile, escapechar='\\', doublequote=True)
        result = []
        for row in parserDict:
            array = []
            for i in data.getAttributs():
                try:
                    tmp = row[i[0]].strip()
                    array.append(tmp if tmp.isnumeric() else "\"" + tmp.replace("\"", "\\\"") + "\"")
                except KeyError:
                    print ("La clé " + i + "n'existe pas")
            result.append(array)
        return result

    def addDataBase(self,data):
        """ Permet d'ajouter les données récupérées avec la méthode create dans la base de données 
        param : un objet Data """
        array = CreateFromCSV.create(data)
        for row in array:
            request = "Insert into " + data.getNomTable() + " values ("
            for value in row:
                request += value +", "
            request = request[:len(request)-2]
            request += ")"
            self.db.insert(request)
        self.db.commit()


    def createTables(self,data):
        """ Permet de créer les différentes tables dans la base de données 
        Cette méthode n'est appellée qu'une seule fois (au début) dans le fichier Application.py """
        request = "Create table " + data.getNomTable() + "("
        for attributs in data.getAttributs():
            request += "`" + attributs[0].replace("\'", " ") + "` "+ attributs[1]+","
        request = request[:len(request)-1]
        request += ")"
        self.db.insert(request)
        self.db.commit()
