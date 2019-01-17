from enum import Enum
class Rdv:
    def __init__(self,bien, type,date,acheteur=None,vendeur=None):
        self.acheteur =acheteur
        self.vendeur = vendeur
        self.bien = bien
        self.type = type
        self.date = date

class TypesRdv(Enum):
    VENTE = 1
    MANDAT = 2
    VISITE = 3