import re
from src.IHM.DialBien import DialBien
from src.IHM.DialAchatBien import  DialAchatBien
regXchoice = "[123]"

class ctrlModifPersonne:
    def __init__(self,agence,personne):
        self.agence = agence
        self.personne = personne
    def nomPers(self):
        return self.personne.nom
    def validateInputChoice(self,choice):
        return re.fullmatch(regXchoice,choice)
    def submitChoice(self,choice):
        if choice == "1":
            DialBien(self.agence,self.personne)
        elif choice == "2":
            DialAchatBien(self.agence,self.personne)
        elif choice == "3":
            ...#Rdv