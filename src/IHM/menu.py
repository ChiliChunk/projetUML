import re
import src.IHM.listePersonnes as lstPers
import src.IHM.ajoutPersonne as ajtPers

def menu(agence):
    regX123 = "[123]"
    #Faire la serialisation
    print("Faites un choix ")
    print("1) Consulter la liste des personnes")
    print("2) Ajouter une personne")
    print("3) Quitter l'application ")

    while 1:
        choice =input()
        if re.fullmatch(regX123, choice):
            if choice == "1":
                lstPers.listePersonnes(agence)
            elif choice == "2":
                ajtPers.ajoutPersonne(agence)
            elif choice == "3":
                ...
                #main.save(agence)
        else:
            print("Veuillez entrez une option valide")

def testo():
    print("testo")