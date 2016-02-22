import csv
from MySQL import DataBase as db

class Installation(object):
    def __init__(self, dic):
        self.name = dic["Nom usuel de l'installation"]
        self.city = dic["Nom de la commune"]
        self.code = dic["Code INSEE"]
        self.db = new db()
    def toString(self):
        return (self.name + " " + self.city + "  " + self.code)
    def ajoutDB(self):
        self.db.insertQuerry("insert into installation")

class Activite(object):
    def __init__(self, dic):
        self.ComInsee = dic["ComInsee"]
        self.ComLib = dic["ComLib"]
        self.EquipementId = dic ["EquipementId"]
        self.EquNbEquIdentique = dic["EquNbEquIdentique"]
        self.ActCode = dic["ActCode"]
        self.ActLib = dic["ActLib"]
        self.EquActivitePraticable = dic["EquActivitePraticable"]
        self.EquActivitePratique = dic["EquActivitePratique"]
        self.EquActiviteSalleSpe = dic["EquActiviteSalleSpe"]
        self.ActNivLib = dic["ActNivLib"]
    def toString(self):
        return (self.ComInsee + " " + self.ComLib + " " + self.EquipementId + " " + self.EquNbEquIdentique + " " + self.ActCode + " " + self.ActLib + " " + self.EquActivitePraticable + " " +  self.EquActivitePratique  + " " + self.EquActiviteSalleSpe + " " + self.ActNivLib)
    def ajoutDB(self):


class Equipement(object):
    def __init__(self, dic):
        self.ComInsee = dic["ComInsee"]
        self.ComLib = dic["ComLib"]
        self.InsNumeroInstall = dic["InsNumeroInstall"]
        self.InsNom = dic["InsNom"]
        self.EquId = dic["EquipementId"]
        self.EquNom = dic["EquNom"]
        self.EquNomBatiment = dic["EquNomBatiment"]
    def toString(self):
        return (self.ComInsee + " " +self.ComLib + " " +self.InsNumeroInstall + " " +self.InsNom + " " +self.EquId+ " " +self.EquNom + " " +self.EquNomBatiment);


class Parser(object):

    def __init__(self, file, dataToGet, classe):
        self.file = file
        self.dataToGet = dataToGet
        self.classe = classe

    def parser(self):
        dataFile = open(self.file, "r")
        parserDict = csv.DictReader(dataFile)
        result = []
        constructor = globals()[self.classe]
        for row in parserDict:
            dic ={}
            for i in self.dataToGet:
                try:
                    dic[i] = row[i]
                except KeyError:
                    print ("La clé " + i + "n'existe pas")
            result.append(constructor (dic))
        return result


data = ["Nom usuel de l'installation", "Nom de la commune", "Code INSEE"]
parser1 = Parser("installation.csv", data,"Installation")
parser2 = Parser("equipements.csv",["ComInsee", "ComLib", "InsNumeroInstall", "InsNom", "EquipementId", "EquNom", "EquNomBatiment"],"Equipement")
result1 = parser1.parser()
result2 = parser2.parser()
for i in result2:
    print (i.toString())
    print ("\n")
