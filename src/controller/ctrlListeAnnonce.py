from src.IHM.Menu import Menu
import re

regChoice = "[0-9]+"

class ctrlListeAnnonce:
    def __init__(self, agence):
        self.agence = agence
        self.annonces = self.agence.annonces

    def validateInputChoice(self, choice):
        return re.fullmatch(regChoice, choice)

    def processChoice(self, choice):
        if choice == "0":
            Menu(self.agence)
        else:
            ...


