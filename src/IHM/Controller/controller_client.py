from src.IHM.Controller.controller_bien import ControllerBien


class ControllerClient:

    @staticmethod
    def menu(agence):
        print(agence.personnes)
        working = True
        while working:
            choix = input("\n\n"
                      "     A: Ajouter un client\n"
                      "     V: Ajouter un voeux\n"
                      "     B: Ajouter un bien\n"
                      "     S: Supprimer un client\n"
                      "     R: Retour")

            if choix == "A":
                ControllerClient.ajouterClient(agence)
            elif choix == "V":
                personne = input("A quel client ?")
                if personne in agence.personnes:
                    ControllerVoeux.ajouterVoeux(agence, personne)
                else :
                    print("Client inconnu(e)")
            elif choix == "B":
                personne = input("A quel client ?")
                if personne in agence.personnes:
                    ControllerBien.ajouterBien(agence, personne)
                else:
                    print("Client inconnu(e)")
            elif choix == "S":
                personne = input("A quel client ?")
                if personne in agence.personnes:
                    ControllerClient.supprimer(agence, personne)
                else:
                    print("Client inconnu(e)")
            elif choix == "R":
                working = False
            else:
                print("Choix invalide")

    @staticmethod
    def ajouterClient(agence):
        working = True
        while working:
            type = input("Quel type de client ?\n"
                     "  P: personne physique\n"
                     "  M: personne morale\n"
                     "  R: Retour\n")
            if type == "P":
                print("TODO")
            elif type == "M":
                print("TODO")
            elif type == "R":
                working = False
            else:
                print("Choix invalide")

    @staticmethod
    def supprimer(agence, personne):
        agence.personnes.remove(personne)
        print("Client supprimé")

