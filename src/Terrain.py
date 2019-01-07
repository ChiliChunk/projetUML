from src import BienImmobilier as B

class Terrain(B.BienImmobilier):
    def __init__(self,prix,dateVente,adresse,orientation,dateDispo,surfaceSol,longueurFacade, id ):
        super().__init__(self,prix,dateVente,adresse,orientation,dateDispo,id)
        self.surfaceSol = surfaceSol
        self.longueurFacade = longueurFacade


