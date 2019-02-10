from src.Model.BienImmobilier import BienImmobilier,TypesBien

class Appartement(BienImmobilier):
    def __init__(self,prix,dateVente,adresse,orientation,dateDispo,vendeur, nbPiece,numEtage, chargesMensuelles):
        super().__init__(prix,dateVente,adresse,orientation,dateDispo, vendeur)
        self.nbPiece = nbPiece
        self.numEtage = numEtage
        self.chargesMensuelles = chargesMensuelles
        self.type = TypesBien.APPARTEMENT

    def __str__(self):
        result = super.__str__()
        result += f"orientation : {self.orientation}\n"
        result += f"date dispo: {self.dateDispo}\n"
        result += f"nombre Piece: {self.nbPiece}\n"
        result += f"num d etage: {self.numEtage}\n"
        return result