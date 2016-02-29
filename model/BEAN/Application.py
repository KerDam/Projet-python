from CreateFromCSV import CreateFromCSV
from Data import Data
#Application qui met en relation les différentes classes Data, CreateFromCSV et Dao

""" Création des différents Data
	ex : Pour enregistrer une installations
	- on va chercher les informations dans le fichier installations.csv
	- on stock les informations dans la table installations de la base de données
	- les différents attributs sont précisés dans attributsInstallation """

#attributsInstallation = ["Nom usuel de l'installation", "Numéro de l'installation", "Nom de la commune", "Code INSEE", "Code postal", "Nom du lieu dit", "Numero de la voie", "Nom de la voie", "location", "Longitude", "Latitude"]
#dataInstallation = new Data("installations", "installations", attributsInstallation)

# attributsActivite = ["ComInsee", "ComLib", "EquipementId", "EquNbEquIdentique", "ActCode", "ActLib", "EquActivitePraticable", "EquActivitePratique", "EquActiviteSalleSpe", "ActNivLib"]
# dataActivite = new Data("activites", "activites", attributsActivite)

attributsEquipement = ["ComInsee", "ComLib", "InsNumeroInstall", "InsNom", "EquipementId", "EquNom", "EquNomBatiment", "EquipementTypeLib", "EquipementFiche", "FamilleFicheLib"]
dataEquipement = Data("../../donnees/equipements.csv", "equipements", attributsEquipement)

#CreateFromCSV.addDataBase(dataEquipement)
CreateFromCSV.createTables(dataEquipement)
