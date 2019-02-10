import re
import src.IHM.AjoutPersonne as ajt
import src.IHM.init as main
from src.IHM.ListeComposants import ListeComposants
from src.IHM.ModifPersonne import ModifPersonne
regXchoice = "[123]"


class ctrlMenu:
    def __init__(self,agence):
        self.agence =agence

    def validateInputChoice(self,choice):
        return re.fullmatch(regXchoice,choice)
    def chooseOption(self,choice):
        if choice == "1":
            list = ListeComposants(self.agence,1)
            pers = list.view()
            ModifPersonne(agence=self.agence,personne=pers)
            #lst.ListePersonnes(self.agence)
        elif choice == "2":
            ajt.AjoutPersonne(self.agence)
        elif choice == "3":
            main.save(self.agence)
            exit(0)
