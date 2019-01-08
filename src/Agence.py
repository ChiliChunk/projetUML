from src.Rdv import Rdv,TypesRdv
class Agence:
    def __init__(self , nom="Agence Par defaut"):
        self.rdvs = []
        self.biensImmobiliers = []
        self.annonces = []
        self.personnes = []
        self.nom = nom

    def prendreRdvMandat(self, bien,date):
        self.rdvs.append(Rdv(bien=bien,vendeur=bien.vendeur, type=TypesRdv.MANDAT,date=date))

    def prendreRdvVente(self, bien, date, acheteur):
        ...
        #self.rdvs.append(Rdv(bien=bien,vendeur=bien.vendeur, type=TypesRdv.VENTE,date=date))

    def prendreRdvVisite(self, bien,date, visiteur):
        ...
        #self.rdvs.append(Rdv(bien=bien,vendeur=bien.vendeur, type=TypesRdv.VISITE,date=date))

    def __str__(self):
        return (f"rdvs : {''.join(str(e) for e in self.rdvs)} biens : {''.join(str(e) for e in self.biensImmobiliers)} annonces : {''.join(str(e) for e in self.annonces)} personnes : {''.join(str(e) for e in self.personnes)} NOM : {self.nom}")
