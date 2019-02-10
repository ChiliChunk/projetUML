from src.BienImmobilier import BienImmobilier


class Terrain(BienImmobilier):
    def __init__(self, prix, dateVente, adresse, orientation, dateDispo, vendeur, surfaceSol, longueurFacade):
        super().__init__(prix, dateVente, adresse, orientation, dateDispo, vendeur)
        self.surfaceSol = surfaceSol
        self.longueurFacade = longueurFacade
        self.type = BienImmobilier.TypesBien.TERRAIN

    def __str__(self):
        result = "Type : TERRAIN \n"
        result += f"prix : {self.prix}\n"
        result += f"date de vente : {self.dateVente}\n"
        result += f"adresse: {self.adresse}\n"
        result += f"orientation : {self.orientation}\n"
        result += f"date dispo: {self.dateDispo}\n"
        result += f"surface: {self.surfaceSol}\n"
        return result
