import re
import src.IHM.AjoutPersonne as ajt
import src.IHM.ListePersonnes as lst
import src.IHM.init as main
regXchoice = "[123]"


class ctrlMenu:
    def __init__(self,agence):
        self.agence =agence

    def validateInputChoice(self,choice):
        return re.fullmatch(regXchoice,choice)
    def chooseOption(self,choice):
        if choice == "1":
            lst.ListePersonnes(self.agence)
        elif choice == "2":
            ajt.AjoutPersonne(self.agence)
        elif choice == "3":
            main.save(self.agence)
            exit(0)
