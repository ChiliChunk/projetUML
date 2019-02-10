from src.Model.Physique import Physique # pour le main de test
from src.Model.Agence import Agence # pour le main de test
from src.Model.Maison import Maison # pour le main de test

from src.controller.CtrlDialAchatBien import CtrlDialAchatBien

class DialAchatBien:
    def __init__(self , personne , agence):
        self.ctrl = CtrlDialAchatBien(personne , agence)
        self.askType()


    def askType(self):
        valid = False
        while not valid:
            type = input('Veuillez entrer un type de voeux:\n'
                         '1 : Appartement\n'
                         '2 : Maison\n'
                         '3 : Terrain\n')
            valid = self.ctrl.validateType(type)

        self.type = int(type)
        self.askStaticData()
        self.askDynamicData(type)

    def askStaticData(self):
        valid = False
        prix = None
        localisation = None
        while not valid:
            prix = input('Veuillez entrer un prix max souhaité en €: ')
            valid = self.ctrl.validateNumber(prix)
        self.prix = int(prix)
        valid = False
        while not valid:
            localisation = input('Veuillez entrer une localisation: ')
            valid = self.ctrl.validateString(localisation)
        self.localisation = localisation


    def submit(self):
        biens = self.ctrl.attachToPers(self.type,self.prix,self.localisation,self.surface,self.nombrePiece)
        if len(biens) > 0:
            lesBiens = "Les biens qui correspondent a votre voeux: \n"
            for bien in biens:
                lesBiens += bien.__str__()
            print(lesBiens)
        else:
            print("Aucun bien enregistrés non correspond a votre voeux")

    def askDynamicData(self,type):
        self.nombrePiece = None
        self.surface = None
        if self.type == 1 or self.type == 2 :#appartement ou maison
            valid = False
            TestNombrePiece = None
            while not valid:
                TestNombrePiece = input('Veuillez entrer un nombre de piece: ')
                valid = self.ctrl.validateNumber(TestNombrePiece)
            self.nombrePiece = int(TestNombrePiece)

        if self.type == 3 or self.type == 2:#terrain ou maison
            valid = False
            TestSurface = None
            while not valid:
                TestSurface = input('Veuillez entrer une surface en m²: ')
                valid = self.ctrl.validateNumber(TestSurface)
            self.surface = int(TestSurface)
            self.submit()


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
    pers = Physique("Nom", "add","0123456789","test@osef.fr")
    agence = Agence()
    maison = Maison(3,"osef","osef","osef","osef",3,3,"osef","osef","osef")
    agence.biensImmobiliers.append(maison)
    dial = DialAchatBien(pers , agence)
