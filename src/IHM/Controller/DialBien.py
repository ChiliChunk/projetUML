from src.Physique import Physique  # pour le main de test
from src.Agence import Agence  # pour le main de test
from src.Maison import Maison  # pour le main de test

from src.IHM.Controller.CtrlDialBien import CtrlDialBien


class DialBien:
    def __init__(self, personne, agence):
        self.ctrl = CtrlDialBien(personne, agence)
        self.askType()

    def askType(self):
        valid = False
        while not valid:
            type = input('Veuillez entrer un type de Bien:\n'
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
        date = None
        test_orientation = None
        while not valid:
            prix = input('Veuillez entrer un prix max souhaité en €: ')
            valid = self.ctrl.validateNumber(prix)
        self.prix = int(prix)
        valid = False
        while not valid:
            localisation = input('Veuillez entrer une localisation: ')
            valid = self.ctrl.validateString(localisation)
        self.localisation = localisation
        valid = False
        while not valid:
            date = input("Date de disponibilité (DD/MM/AAAA: ")
            valid = self.ctrl.validateDate(date)
        self.dateDispo = date
        valid = False
        while not valid:
            test_orientation = input("Oriantation (N,S,E,O) : ")
            valid = self.ctrl.validateOrientation(test_orientation)
        self.orientation = test_orientation

    def submit(self):
        biens = self.ctrl.attachToPers(self.type, self.prix, None, self.localisation, self.orientation, self.dateDispo,
                                       self.surface, self.nombrePiece, self.nb_etage, self.moyen_de_chauffage,
                                       self.longueur_facade, self.num_etage, self.charge_mensuelles)
        if len(biens) > 0:
            lesBiens = "Les biens qui correspondent a votre voeux: \n"
            for bien in biens:
                lesBiens += bien.__str__()
            print(lesBiens)
        else:
            print("Aucun bien enregistrés non correspond a votre voeux")

    def askDynamicData(self, type):
        self.nombrePiece = None
        self.surface = None
        test_longueur_facade = None
        test_nb_etage = None
        test_charge_mensuelles = None
        test_num_etage = None
        if self.type == 1 or self.type == 2:  # appartement ou maison
            valid = False
            TestNombrePiece = None
            while not valid:
                TestNombrePiece = input('Veuillez entrer un nombre de piece: ')
                valid = self.ctrl.validateNumber(TestNombrePiece)
            self.nombrePiece = int(TestNombrePiece)
        if self.type == 1:
            valid = False
            while not valid:
                test_num_etage = input("Entrer l'étage : ")
                valid = self.ctrl.validateNumber(test_num_etage)
            valid = False
            while not valid:
                test_charge_mensuelles = input("Montant des charges mensuelles en € : ")
                valid = self.ctrl.validateNumber(test_charge_mensuelles)
            self.num_etage = int(test_num_etage)
            self.charge_mensuelles = int(test_charge_mensuelles)

        if self.type == 2:
            valid = False
            while not valid:
                test_nb_etage = input("Nombre d'étage de la maison : ")
                valid = self.ctrl.validateNumber(test_nb_etage)
            self.nb_etage = int(test_nb_etage)
            self.moyen_de_chauffage = input("Moyen de chauffage de la maison : ")

        if self.type == 3 or self.type == 2:  # terrain ou maison
            valid = False
            TestSurface = None
            while not valid:
                TestSurface = input('Veuillez entrer une surface en m²: ')
                valid = self.ctrl.validateNumber(TestSurface)
            self.surface = int(TestSurface)
            self.submit()

        if self.type == 3:
            valid = False
            while not valid:
                test_longueur_facade = input("Longueur de la facade du terrain en m : ")
                valid = self.ctrl.validateNumber(test_longueur_facade)
            self.longueur_facade = int(test_longueur_facade)

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
    pers = Physique("Nom", "add", "0123456789", "test@osef.fr")
    agence = Agence()
    maison = Maison(3, "osef", "osef", "osef", "osef", 3, 3, "osef", "osef", "osef")
    agence.biensImmobiliers.append(maison)
    dial = DialBien(pers, agence)
