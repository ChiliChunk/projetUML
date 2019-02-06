from src.Voeux import Voeux
from src.BienImmobilier import BienImmobilier

class CtrlDialBien:


    def __init__(self,personne, agence):
        self.personne = personne
        self.agence = agence


    def attachToPers (self,type,prix,localisation,surface,nombrePiece):
        tempType = BienImmobilier.TypesBien.APPARTEMENT
        if type == 2:
            tempType = BienImmobilier.TypesBien.MAISON

        elif type == 3:
            tempType = BienImmobilier.TypesBien.TERRAIN
        monVoeux = BienImmobilier(tempType , prix,localisation,surfaceAuSol=surface , nombrePiece=nombrePiece)
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