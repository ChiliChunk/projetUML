from enum import Enum
class BienImmobilier :

    class TypesBien(Enum):
        MAISON =1
        APPARTEMENT =2
        TERRAIN =3

    def __init__(self, prix,dateVente,adresse,orientation,dateDispo,id, vendeur):
        self.prix = prix
        self.dateVente = dateVente
        self.adresse = adresse
        self.orientation = orientation
        self.dateDispo = dateDispo
        self.id = id
        self.vendeur = vendeur

    def inscrire (self,agence):
        agence.biensImmobiliers.append(self)