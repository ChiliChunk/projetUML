from src.Model.BienImmobilier import BienImmobilier, TypesBien

class Maison(BienImmobilier):
    def __init__(self,prix,dateVente,adresse,orientation,dateDispo,vendeur, surface, nbPiece,nbEtage,moyenChauffage):
        super().__init__(prix,dateVente,adresse,orientation,dateDispo,vendeur)
        self.surface = surface
        self.nbPiece = nbPiece
        self.nbEtage = nbEtage
        self.moyenChauffage = moyenChauffage
        self.type = TypesBien.MAISON

    def __str__(self):
        result = super.__str__(self)
        result += f"orientation : {self.orientation}\n"
        result += f"date dispo: {self.dateDispo}\n"
        result += f"surface: {self.surface}\n"
        result += f"nombre Piece: {self.nbPiece}\n"
        result += f"nombre d etage: {self.nbEtage}\n"
        result += f"moyen de chauffage: {self.moyenChauffage}\n"
        return result

