import re
import src.IHM.Menu as men
regXnbPersonnes = "[0-9]+"

class ctrlListePersonnes:
    def __init__(self,agence):
        self.agence = agence
        self.personnes = self.agence.personnes

    def validateInputChoice(self,choice):
        return re.fullmatch(regXnbPersonnes,choice)

    def processChoice(self,choice):
        if choice=="0":
            men.Menu(self.agence)
        else:
            ...#ModifPersonne(self.agence,personnes[choice-1])