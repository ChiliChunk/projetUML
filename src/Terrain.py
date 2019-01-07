from src import BienImmobilier as B

class Terrain(B.BienImmobilier):
    def __init__(self,prix,dateVente,adresse,orientation,dateDispo,surfaceSol,longueurFacade ):
        super().__init__(self,prix,dateVente,adresse,orientation,dateDispo)
        self.surfaceSol = surfaceSol
        self.longueurFacade = longueurFacade


