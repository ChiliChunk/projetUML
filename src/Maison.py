from src.BienImmobilier import BienImmobilier

class Maison(BienImmobilier):
    def __init__(self,prix,dateVente,adresse,orientation,dateDispo, surface, nbPiece,nbEtage,moyenChauffage, id):
        super().__init__(self,prix,dateVente,adresse,orientation,dateDispo,id)
        self.surface = surface
        self.nbPiece = nbPiece
        self.nbEtage = nbEtage
        self.moyenChauffage = moyenChauffage
        self.type = BienImmobilier.TypesBien.MAISON

