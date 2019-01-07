from src import BienImmobilier as B

class Maison(B.BienImmobilier):
    def __init__(self,prix,dateVente,adresse,orientation,dateDispo, surface, nbPiece,nbEtage,moyenChauffage):
        super().__init__(self,prix,dateVente,adresse,orientation,dateDispo)
        self.surface = surface
        self.nbPiece = nbPiece
        self.nbEtage = nbEtage
        self.moyenChauffage = moyenChauffage
