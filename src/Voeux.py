from src.BienImmobilier import BienImmobilier

class Voeux:

    def __init__(self , typeBien , prixSouhaite , localisation , nombrePiece=None , surfaceAuSol=None):
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
