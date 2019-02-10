import re
import src.IHM.DialAchatBien as dial
import src.IHM.PriseRdv as rdv
regXchoice = "[123]"

class ctrlModifPersonne:
    def __init__(self,agence,personne):
        self.agence =agence
        self.personne = personne
    def nomPers(self):
        return self.personne.nom
    def validateInputChoice(self,choice):
        return re.fullmatch(regXchoice,choice)
    def submitChoice(self,choice):
        if choice == "1":
            ...#AjoutBien
        elif choice == "2":
            dial.DialAchatBien(personne=self.personne,agence=self.agence)
        elif choice == "3":
            rdv.PriseRdv(self.agence,self.personne)