import src.controller.ctrlPriseRdv as ctrl
class PriseRdv:
    def __init__(self,agence,personne):
        self.ctrl = ctrl.ctrlPriseRdv(agence,personne)
        self.view()
    def view(self):
        print("Prise de rendez vous pour "+ str(ctrl.personne))
        choice =input("Selectionner type de RDV\n"
                      "1)Vente\n"
                      "2)Mandat\n"
                      "3)Visite\n")
        while 1:
            if self.ctrl.validateInputChoice(choice):
                break
            else:
                choice = input("Veuillez choisir une option valide\n")
        #Use of controller and then test directly ?..
        if choice =="1":
            self.inputVente()
        if choice=="2":
            self.inputMandat()
        if choice =="3":
            self.inputVisite()

    def inputVente(self):
        date = self.inputDate()

    def inputMandat(self):
        date = self.inputDate()

    def inputVisite(self):
        date = self.inputDate()


    def inputDate(self):
        date = input("Veuillez rentrer une date format JJ/MM/AAAA")
        while 1:
            if self.ctrl.validateInputDate(date):
                break
            else:
                date=input("Veuillez rentrer une date valide")
        return date
