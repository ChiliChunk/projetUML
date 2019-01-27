import src.Agence as ag
import re
import src.IHM.menu as men
def listePersonnes(agence):
    i=1
    dicoPers ={}
    print("Liste des personnes : ")
    for pers in agence.personnes:
       print(i,") "+pers.afficherNom())
       dicoPers[i] =pers
       i+=1
    print("Entrez le numero de la personne pour interagir avec elle \n(ou 0 pour revenir au menu) \n")
    regXnbPersonnes = "[0-9]+"
    while 1:
        choice = input()
        if re.fullmatch(regXnbPersonnes,choice):
            if choice == "0":
                men.menu(agence)
            else:
                ...
                #Traitement
        else:
            print("Veuillez entrez une option valide")