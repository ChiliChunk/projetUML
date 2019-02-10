import src.IHM.ListePersonnes as lstPers
import src.IHM.AjoutPersonne as ajtPers
import src.controller.ctrlMenu as ctrl
class Menu:
    def __init__(self, agence):
        self.ctrl = ctrl.ctrlMenu(agence)
        self.askChoice()

    def askChoice(self):
        choice =input("Faites un choix \n"
                        "1) Consulter la liste des personne)\n"
                        "2) Ajouter une personne\n"
                        "3) Quitter l'application\n ")
        valid = self.ctrl.validateInputChoice(choice)
        while not valid:
            choice = input("Veuillez rentrez une option valide")
            valid = self.ctrl.validateInputChoice(choice)
        self.ctrl.chooseOption(choice)
