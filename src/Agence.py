from src.Rdv import Rdv,TypesRdv
from src.BienImmobilier import BienImmobilier
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

    def checkVoeux (self , voeux):
        result = []
        for bien in self.biensImmobiliers:
            if self._voeuxEqualsBiens(voeux,bien):
                result.append(bien)
        return result

    @classmethod
    def _voeuxEqualsBiens(cls , voeux, bien):
        if voeux.typeBien == bien.type: #si le voeux et le bien sont du meme type
            if voeux.prixSouhaite >= bien.prix: # et que le prix bien est egale ou inferieur au prix souhaité
                if voeux.typeBien == BienImmobilier.TypesBien.MAISON: # si le voeux est une maison
                    if voeux.surfaceAuSol == bien.surface and voeux.nombrePiece == bien.nbPiece:
                        return True
                elif voeux.typeBien == BienImmobilier.TypesBien.APPARTEMENT:
                    if voeux.nombrePiece == bien.nbPiece:
                        return True
                elif voeux.typeBien == BienImmobilier.TypesBien.TERRAIN:
                    if voeux.surfaceAuSol == bien.surface:
                        return True
        return False
    
    def __str__(self):
        return (f"rdvs : {''.join(str(e) for e in self.rdvs)} biens : {''.join(str(e) for e in self.biensImmobiliers)} annonces : {''.join(str(e) for e in self.annonces)} personnes : {''.join(str(e) for e in self.personnes)} NOM : {self.nom}")
