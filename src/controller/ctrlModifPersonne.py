import re
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
            ...#AjoutVoeux
        elif choice == "3":
            ...#PriseRdv