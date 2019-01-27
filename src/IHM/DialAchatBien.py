from src.Physique import Physique
from src.Voeux import Voeux
from src.BienImmobilier import BienImmobilier
from src.controller.CtrlDialAchatBien import *
class DialAchatBien:
    def __init__(self , personne , agence):
        self.askType()
        self.personne = personne
        self.agence = agence


    def askType(self):
        valid = False
        while not valid:
            type = input('Veuillez entrer un type de voeux:\n'
                         '1 : Appartement\n'
                         '2 : Maison\n'
                         '3 : Terrain\n')
            valid = validateType(type)
            
        self.type = int(type)
        self.askStaticData()
        self.askDynamicData(type)

    def askStaticData(self):
        valid = False
        prix = None
        localisation = None
        while not valid:
            prix = input('Veuillez entrer un prix max souhaité en €: ')
            valid = validateNumber(prix)
        self.prix = prix
        valid = False
        while not valid:
            localisation = input('Veuillez entrer une localisation: ')
            valid = validateString(localisation)
        self.localisation = localisation

    def askDynamicData(self,type):
        if self.type == 1 or self.type == 2 :#appartement ou maison
            valid = False
            nombrePiece = None
            while not valid:
                nombrePiece = input('Veuillez entrer un nombre de piece: ')
                valid = validateNumber(nombrePiece)
            self.nombrePiece = int(nombrePiece)

        if self.type == 3 or self.type == 2:#terrain ou maison
            valid = False
            surface = None
            while not valid:
                surface = input('Veuillez entrer une surface en m²: ')
                valid = validateNumber(surface)
            self.surface = int(surface)

    def __str__(self):
        result = f"Type : {self.type}\n"
        result += f"Prix : {self.prix}\n"
        result += f"Localisation : {self.localisation}\n"
        if self.type == 1 or self.type == 2:
            result += f"Nombre de Piece : {self.nombrePiece}\n"
        if self.type == 3 or self.type == 2:
            result += f"Surface : {self.surface}\n"
        return result


if __name__ == '__main__':
    dial = DialAchatBien(None,None)
    print(dial)