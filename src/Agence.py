from src.Rdv import Rdv,TypesRdv
from src.Mandat import Mandat
from src.PromesseDeVente import PromesseDeVente
class Agence:
    def __init__(self , nom="Agence Par defaut"):
        self.rdvs = []
        self.biensImmobiliers = []
        self.annonces = []
        self.personnes = []
        self.nom = nom

    def prendreRdvMandat(self, bien,date):
        self.rdvs.append(Rdv(bien=bien,vendeur=bien.vendeur, type=TypesRdv.MANDAT,date=date))
        #return Mandat(Personne=bien.vendeur, BienImmobilier=bien)

    def prendreRdvVente(self, bien, date, acheteur):
        ...
        #self.rdvs.append(Rdv(bien=bien,vendeur=bien.vendeur,acheteur=acheteur, type=TypesRdv.VENTE,date=date))
        #return PromesseDeVente()

    def prendreRdvVisite(self, bien,date, visiteur):
        ...
        #self.rdvs.append(Rdv(bien=bien,vendeur=bien.vendeur, type=TypesRdv.VISITE,date=date))

    def __str__(self):
        return (f"rdvs : {''.join(str(e) for e in self.rdvs)} biens : {''.join(str(e) for e in self.biensImmobiliers)} annonces : {''.join(str(e) for e in self.annonces)} personnes : {''.join(str(e) for e in self.personnes)} NOM : {self.nom}")
