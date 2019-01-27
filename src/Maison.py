from src.BienImmobilier import BienImmobilier

class Maison(BienImmobilier):
    def __init__(self,prix,dateVente,adresse,orientation,dateDispo, surface, nbPiece,nbEtage,moyenChauffage, id):
        super().__init__(prix,dateVente,adresse,orientation,dateDispo,id)
        self.surface = surface
        self.nbPiece = nbPiece
        self.nbEtage = nbEtage
        self.moyenChauffage = moyenChauffage
        self.type = BienImmobilier.TypesBien.MAISON

    def __str__(self):
        result = "Type : MAISON \n"
        result += f"prix : {self.prix}\n"
        result += f"date de vente : {self.dateVente}\n"
        result += f"adresse: {self.adresse}\n"
        result += f"orientation : {self.orientation}\n"
        result += f"date dispo: {self.dateDispo}\n"
        result += f"surface: {self.surface}\n"
        result += f"nombre Piece: {self.nbPiece}\n"
        result += f"nombre d etage: {self.nbEtage}\n"
        result += f"moyen de chauffage: {self.moyenChauffage}\n"
        return result
