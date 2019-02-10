from enum import Enum
from src.controller.ctrlListeComposants import ctrlListeComposants
class ListeComposants :
    def __init__(self,agence, type, personne= None):
        self.ctrl= ctrlListeComposants(agence,type,personne)

    def view(self):
        i = 1
        for compo in self.ctrl.compos:
            print(i, ") " + str(compo))
            i+=1
        print("Entrez le numero pour interagir avec cette option \n(ou 0 pour revenir au menu) \n")
        while 1:
            choice = input()
            if self.ctrl.validateInputChoice(choice):
                break
            else:
                print("Veuillez entrez une option valide")
        return self.ctrl.submitChoice(choice)