from src import Bien

class Terrain(Bien.BienImmobilier):
    def __init__(self,prix,dateVente,adresse,orientation,dateDispo,surfaceSol,longueurFacade ):
        super().__init__(self,prix,dateVente,adresse,orientation,dateDispo)
        self.surfaceSol = surfaceSol
        self.longueurFacade = longueurFacade


