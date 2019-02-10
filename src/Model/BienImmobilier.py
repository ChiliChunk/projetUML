from enum import Enum
class BienImmobilier :
    def __init__(self, prix, dateVente, adresse, orientation, dateDispo, vendeur):
        self.prix = prix
        self.dateVente = dateVente
        self.adresse = adresse
        self.orientation = orientation
        self.dateDispo = dateDispo
        self.id = id
        self.vendeur = vendeur

    def inscrire(self, agence):
        agence.biensImmobiliers.append(self)

    def __str__(self):
        result = "Type : "+self.__class__.__name__+"\n"
        result += f"prix : {self.prix}\n"
        if self.dateVente:
            result += f"VENDU \n date de vente : {self.dateVente}\n"
        result += f"adresse: {self.adresse}\n"
class TypesBien(Enum):
    MAISON =1
    APPARTEMENT =2
    TERRAIN =3