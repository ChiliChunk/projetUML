from src.BienImmobilier import BienImmobilier

class Appartement(BienImmobilier):
    def __init__(self,prix,dateVente,adresse,orientation,dateDispo, nbPiece,numEtage, chargesMensuelles, id):
        super().__init__(self,prix,dateVente,adresse,orientation,dateDispo, id)
        self.nbPiece = nbPiece
        self.numEtage = numEtage
        self.chargesMensuelles = chargesMensuelles
        self.type = BienImmobilier.TypesBien.APPARTEMENT

