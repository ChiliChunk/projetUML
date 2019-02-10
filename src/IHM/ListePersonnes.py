import src.controller.ctrlListePersonnes as ctrl
class ListePersonnes:

    def __init__(self,agence):
        self.ctrl = ctrl.ctrlListePersonnes(agence)
        self.listePersonnes()

    def listePersonnes(self):
        i=1
        print("Liste des personnes : ")
        for pers in self.ctrl.personnes:
           print(i,") "+str(pers))
        print("Entrez le numero de la personne pour interagir avec elle \n(ou 0 pour revenir au menu) \n")
        while 1:
            choice = input()
            if self.ctrl.validateInputChoice(choice):
                self.ctrl.processChoice(choice)
            else:
                print("Veuillez entrez une option valide")