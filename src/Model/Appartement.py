from src.Model.BienImmobilier import BienImmobilier

class Appartement(BienImmobilier):
    def __init__(self,prix,dateVente,adresse,orientation,dateDispo,vendeur, nbPiece,numEtage, chargesMensuelles):
        super().__init__(prix,dateVente,adresse,orientation,dateDispo, vendeur)
        self.nbPiece = nbPiece
        self.numEtage = numEtage
        self.chargesMensuelles = chargesMensuelles
        self.type = BienImmobilier.TypesBien.APPARTEMENT

    def __str__(self):
        result = "Type : TERRAIN \n"
        result += f"prix : {self.prix}\n"
        result += f"date de vente : {self.dateVente}\n"
        result += f"adresse: {self.adresse}\n"
        result += f"orientation : {self.orientation}\n"
        result += f"date dispo: {self.dateDispo}\n"
        result += f"surface: {self.surface}\n"
        result += f"nombre Piece: {self.nbPiece}\n"
        result += f"num d etage: {self.numEtage}\n"
        return result