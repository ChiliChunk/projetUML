import src.Personne as prs
import re
import src.IHM.menu as men

regXmail ="[^@]+@[^@]+\.[^@]+"
regXTel ="[0-9]{10,15}"

def ajoutPersonne(agence):
    print("\n Bienvenue à la création d'une nouvelle personne")
    nom = input("Entrez le nom : " )
    adresse =input("Entrez l'adresse : ")
    while 1:
        tel = input("Entrez le telephone : ")
        if re.fullmatch(regXTel, tel):
            break
        else:
            print("Entrez un tel valide")
    while 1:
        adresseMail = input("Entrez l'adresse mail :")
        if re.fullmatch(regXmail, adresseMail):
            break
        else:
            print("Entrez un email valide")

    pers = prs.Personne(nom,adresse,tel,adresseMail)
    pers.inscrire(agence)
    print("Personne inscrite !")
    men.menu(agence)