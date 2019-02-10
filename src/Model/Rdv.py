from enum import Enum
from src.Model.PromesseDeVente import PromesseDeVente
class Rdv:
    def __init__(self, type,date,bien=None,acheteur=None,vendeur=None):
        self.acheteur =acheteur
        self.vendeur = vendeur
        self.bien = bien
        self.type = type
        self.date = date

    def genererPromesseVente(self, adresseNotaire,):
        if self.type == TypesRdv.VENTE:
            return PromesseDeVente()

class TypesRdv(Enum):
    VENTE = 1
    MANDAT = 2
    VISITE = 3