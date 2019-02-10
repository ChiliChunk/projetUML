from src.Model.BienImmobilier import BienImmobilier


class Voeux:

    def __init__(self, typeBien, prixSouhaite, localisation, nombrePiece=None, surfaceAuSol=None):
        self.typeBien = typeBien
        self.prixSouhaite = prixSouhaite
        self.localisation = localisation
        if typeBien == BienImmobilier.TypesBien.APPARTEMENT:
            self.nombrePiece = nombrePiece
        if typeBien == BienImmobilier.TypesBien.TERRAIN:
            self.surfaceAuSol = surfaceAuSol
        if typeBien == BienImmobilier.TypesBien.MAISON:
            self.nombrePiece = nombrePiece
            self.surfaceAuSol = surfaceAuSol

    def __str__(self):
        result = ""
        if self.typeBien == BienImmobilier.TypesBien.MAISON:
            result += "Type  : MAISON\n"
        elif self.typeBien == BienImmobilier.TypesBien.APPARTEMENT:
            result += "Type : APPARTEMENT\n"
        else:
            result += "Type : TERRAIN\n"
        result += f"prix : {self.prixSouhaite}\n" \
                  f"localisation : {self.localisation}\n" \
                  f"nombrePiece : {self.nombrePiece}\n" \
                  f"surface au sol : {self.surfaceAuSol}"
        return result