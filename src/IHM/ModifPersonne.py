import src.controller.ctrlModifPersonne as ctrl
class ModifPersonne:
    def __init__(self,agence, personne):
        self.ctrl = ctrl.ctrlModifPersonne(agence,personne)
        self.view()

    def view(self):
        print("Option sur "+str(self.ctrl.personne))
        choice = input("Choissisez une option \n"
                  "1)Ajout bien\n"
                  "2)Ajout Voeux\n"
                  "3)Prise de RDV\n")
        while 1:
            if self.ctrl.validateInputChoice(choice):
                break
            else:
                choice=input("Veuillez choisir une option valide")
        self.ctrl.submitChoice(choice)
