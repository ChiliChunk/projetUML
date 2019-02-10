from src.controller.ctrlListeAnnonce import ctrlListeAnnonce


class ListeAnnonce:
    def __init__(self, agence):
        self.ctrl = ctrlListeAnnonce(agence)

    def listeAnnonce(self):
        i=1
        print("Liste des annonces")
        for an in self.ctrl.annonces:
            print(""+i+") " + str(an))
            i += 1
        print("Entrez le numero de l'annonce à modifier\n"
              "revenir au menu principal avec 0")
        while 1:
            choice = input()
            if self.ctrl.validateInputChoice(choice):
                self.ctrl.processChoice(choice)
            else:
                print("Veuillez entrez une option valide")
