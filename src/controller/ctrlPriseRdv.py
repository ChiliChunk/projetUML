import re
import src.Rdv as rdv
import src.IHM.Menu as men
regXchoice = "[123]"
regXDate = "[0-9]{2}\/[0-9]{2}\/[0-9]{4}"
class ctrlPriseRdv:
    def __init__(self,agence,personne):
        self.agence = agence
        self.personne =personne
    def validateInputChoice(self,choice):
        return re.fullmatch(regXchoice,choice)
    #Need to check day and month valid and after current date
    def validateInputDate(self, date):
        return re.fullmatch(regXDate,date)
    def submitRdv(self, type,date,bien=None,acheteur=None,vendeur=None):
        self.agence.rdvs.append(rdv.Rdv(type=type,date=date,bien=bien,acheteur=acheteur,vendeur=vendeur))
    def redirect(self):
        men.Menu(self.agence)