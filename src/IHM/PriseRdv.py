import src.controller.ctrlPriseRdv as ctrl
import src.IHM.ListeComposants as lst
import src.controller.ctrlListeComposants as lstEnum
import src.Model.Rdv as rdv

class PriseRdv:
    def __init__(self,agence,personne):
        self.ctrl = ctrl.ctrlPriseRdv(agence,personne)
        self.view()
    def view(self):
        print("Prise de rendez vous pour "+ str(self.ctrl.personne))
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
        if choice == rdv.TypesRdv.VENTE.value:
            self.inputVente()
        elif choice== rdv.TypesRdv.MANDAT.value:
            self.inputMandat()
        elif choice == rdv.TypesRdv.VISITE.value:
            self.inputVisite()
        print("Rdv ajouté")
        self.ctrl.redirect()

    def inputVente(self):
        type= rdv.TypesRdv.VENTE
        date = self.inputDate()
        vendeur = self.ctrl.personne
        print("Veuillez choisir l'acheteur")
        acheteur = self.inputPersonne()
        print("Veuillez selectionner le bien a vendre")
        bien = self.inputBien(vendeur)
        self.ctrl.submitRdv(type,date,bien=bien,acheteur=acheteur,vendeur=vendeur)



    def inputMandat(self):
        type= rdv.TypesRdv.MANDAT
        date = self.inputDate()
        vendeur = self.ctrl.personne
        self.ctrl.submitRdv(type,date)



    def inputVisite(self):
        type= rdv.TypesRdv.VISITE
        date = self.inputDate()
        acheteur = self.ctrl.personne
        print("Selectionnez le bien a visiter")
        bien = self.inputBien()
        self.ctrl.submitRdv(type,date,bien=bien,acheteur=acheteur)

    def inputDate(self):
        date = input("Veuillez rentrer une date format JJ/MM/AAAA")
        while 1:
            if self.ctrl.validateInputDate(date):
                break
            else:
                date=input("Veuillez rentrer une date valide")
        return date

    def inputPersonne(self):
        list =lst.ListeComposants(agence=self.ctrl.agence,type=lstEnum.typeCompo.PERSONNE)
        return list.view()
    def inputBien(self,personne=None):
        list =lst.ListeComposants(agence=self.ctrl.agence,type=lstEnum.typeCompo.BIEN,personne=personne)
        return list.view()