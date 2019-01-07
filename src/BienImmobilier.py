from enum import Enum
class BienImmobilier :
    TypesBien = Enum("Maison","Terrain","Appartement")

    def __init__(self, prix,dateVente,adresse,orientation,dateDispo):
        self.prix = prix
        self.dateVente = dateVente
        self.adresse = adresse
        self.orientation = orientation
        self.dateDispo = dateDispo



