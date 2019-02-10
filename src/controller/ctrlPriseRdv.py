import re
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
        return re.fullmatch(date)