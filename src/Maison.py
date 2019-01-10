from src import BienImmobilier as B

class Maison(B.BienImmobilier):
    def __init__(self,prix,dateVente,adresse,orientation,dateDispo, surface, nbPiece,nbEtage,moyenChauffage, id):
        super().__init__(self,prix,dateVente,adresse,orientation,dateDispo,id)
        self.surface = surface
        self.nbPiece = nbPiece
        self.nbEtage = nbEtage
        self.moyenChauffage = moyenChauffage
