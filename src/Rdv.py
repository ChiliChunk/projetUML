from enum import Enum
class Rdv:
    def __init__(self,acheteur,vendeur,bien, type,date):
        self.acheteur =acheteur
        self.vendeur = vendeur
        self.bien = bien
        self.type = type
        self.date = date
class TypesRdv(Enum):
    VENTE = 1
    MANDAT = 2
    VISITE = 3