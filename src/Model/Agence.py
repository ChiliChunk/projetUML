from src.Model.Rdv import Rdv,TypesRdv
from src.Model.BienImmobilier import BienImmobilier
class Agence:
    def __init__(self , nom="Agence Par defaut"):
        self.rdvs = []
        self.biensImmobiliers = []
        self.annonces = []
        self.personnes = []
        self.nom = nom

    def checkVoeux (self , voeux):
        result = []
        for bien in self.biensImmobiliers:
            if self._voeuxEqualsBiens(voeux,bien):
                result.append(bien)
        return result

    def checkBien(self, bien):
        res = []
        for personne in self.personnes:
            if personne.voeux:
                for voeu in personne.voeux:
                    if self._voeuxEqualsBiens(voeu,bien):
                        res += [voeu]
        return res

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
