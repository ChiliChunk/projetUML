from src.BienImmobilier import BienImmobilier
class Terrain(BienImmobilier):
    def __init__(self,prix,dateVente,adresse,orientation,dateDispo,surfaceSol,longueurFacade, id):
        super().__init__(self,prix,dateVente,adresse,orientation,dateDispo,id)
        self.surfaceSol = surfaceSol
        self.longueurFacade = longueurFacade
        self.type = BienImmobilier.TypesBien.TERRAIN



