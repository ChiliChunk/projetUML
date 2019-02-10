import src.controller.ctrlAjoutPersonne as ctrl


class AjoutPersonne:
    def __init__(self,agence):
        self.ctrl = ctrl.ctrlAjoutPersonne(agence)
        self.inputNew()

    def inputNew(self):
        print("Bienvenue à la création d'une nouvelle personne\n")
        nom = input("Entrez le nom : " )
        adresse =input("Entrez l'adresse : ")
        while 1:
            tel = input("Entrez le telephone : ")
            if self.ctrl.validateInputTel(tel):
                break
            else:
                print("Entrez un tel valide")
        while 1:
            adresseMail = input("Entrez l'adresse mail :")
            if self.ctrl.validateInputMail(adresseMail):
                break
            else:
                print("Entrez un email valide")
        self.ctrl.ajoutPers(nom,adresse,tel,adresseMail)
        print("Personne inscrite !")
        self.ctrl.redirection()