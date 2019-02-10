from src.Model import Terrain, Appartement, Maison
import re
regXDate = "[0-9]{2}\/[0-9]{2}\/[0-9]{4}"

class CtrlDialBien:


    def __init__(self, agence,personne):
        self.personne = personne
        self.agence = agence

    #Why dateVente always None
    def attachToPers (self,type,prix, adresse, orientation, dateDispo, surface=None, nbPiece=None,nbEtage=None,moyenChauffage=None, longueurFacade=None, numEtage=None, chargesMensuelles=None):
        monBien = None
        if type == 1:
            monBien = Appartement.Appartement(prix, None, adresse, orientation, dateDispo, self.personne, nbPiece, numEtage, chargesMensuelles)
        elif type == 2:
            monBien = Maison.Maison(prix, None, adresse, orientation, dateDispo, self.personne, surface, nbPiece, nbEtage, moyenChauffage)
        elif type == 3:
            monBien = Terrain.Terrain(prix, None, adresse, orientation, dateDispo, self.personne, surface, longueurFacade)
        self.bien = monBien
        self.agence.biensImmobiliers.append(monBien)
        return self.agence.checkBien(monBien)


    def validateType(self,type):
        index = -1
        try:
            index = int(type)
        except ValueError:
            return False
        if index < 1 or index > 3:
            return False
        else:
            return True

    def validateNumber(self,number):
        try:
            int(number)
        except ValueError:
            return False
        return int(number) > 0

    def validateDate(self, date):
        if not re.fullmatch(regXDate,date):
            return False
        testdate = date.split("/")
        try:
            jour = int(testdate[0])
            mois = int(testdate[1])
            annee = int(testdate[2])
            if not 32>jour>0 :
                return False
            if not 13>mois>0:
                return False
            #Need to change that !
            if not annee>2018:
                return False
        except ValueError:
            return False
        return True

    def validateOrientation(self, ori):
        ori = ori.upper()
        if ori == "N" or "S" or "E" or "O":
            return True
        return False


    def validateString(self , string):
        return len(string) > 0