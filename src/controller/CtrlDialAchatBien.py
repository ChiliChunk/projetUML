from src.Model.Voeux import Voeux
from src.Model.BienImmobilier import BienImmobilier

class CtrlDialAchatBien:


    def __init__(self,personne, agence):
        self.personne = personne
        self.agence = agence


    def attachToPers (self,type,prix,localisation,surface,nombrePiece):
        tempType = BienImmobilier.TypesBien.APPARTEMENT
        if type == 2:
            tempType = BienImmobilier.TypesBien.MAISON
        elif type == 3:
            tempType = BienImmobilier.TypesBien.TERRAIN
        monVoeux = Voeux(tempType , prix,localisation,surfaceAuSol=surface , nombrePiece=nombrePiece)
        self.voeux = monVoeux
        self.personne.ajoutVoeux(monVoeux)
        return self.agence.checkVoeux(self.voeux)


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

    def validateString(self , string):
        return len(string) > 0

    def removeVoeux(self, voeu):
        for personne in self.agence.personnes:
            for voeux in personne.voeux:
                if voeux == voeu:
                    personne.voeux.remove(voeu)
                    return True
        return False
