from src.Model.BienImmobilier import BienImmobilier


class Terrain(BienImmobilier):
    def __init__(self, prix, dateVente, adresse, orientation, dateDispo, vendeur, surfaceSol, longueurFacade):
        super().__init__(prix, dateVente, adresse, orientation, dateDispo, vendeur)
        self.surfaceSol = surfaceSol
        self.longueurFacade = longueurFacade
        self.type = BienImmobilier.TypesBien.TERRAIN

    def __str__(self):
        result = super.__str__()
        result += f"orientation : {self.orientation}\n"
        result += f"date dispo: {self.dateDispo}\n"
        result += f"surface: {self.surfaceSol}\n"
        return result
