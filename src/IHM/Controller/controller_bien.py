from src.Terrain import Terrain
from src.Appartement import Appartement
from src.Maison import Maison


class ControllerBien:

    @staticmethod
    def menu(agence):
        print(agence.biensImmobiliers)
        working = True
        while working:
            choix = input("     A: Ajouter un bien\n"
                          "     S: Supprimer un bien\n"
                          "     R: Retour\n")
            if choix == "A":
                personne = input("A quel client ?")
                if personne in agence.personnes:
                    ControllerBien.ajouterBien(agence, personne)
                else:
                    print("Client inconnu(e)")
            elif choix == "S":
                bien = input("Quel bien ?")
                if bien in agence.biensImmobiliers:
                    ControllerBien.supprimerBien(agence, bien)
                else:
                    print("Bien inconnu")
            elif choix == "R":
                working = False
            else:
                print("Choix invalide")

    @staticmethod
    def ajouterBien(agence, personne):
        working = True
        while working:
            type = input("Type de bien :\n"
                         "      A: Appartement\n"
                         "      M: Maison\n"
                         "      T: Terrain\n"
                         "      R: Retour\n")
            if type == "A":
                prix = input("Prix :")
                dateVente = input("Date de vente :")
                adresse = input("Adresse :")
                orientation = input("Orientation :")
                dateDispo = input("Disponible jusqu'au :")
                nbPiece = input("Nombre de piece")
                numEtage = input("Etage :")
                chargesMensuelles = input("Charge mensuelles :")
                id = input("Id :")
                a = Appartement(float(prix), dateVente, adresse, orientation, dateDispo, int(nbPiece), int(numEtage),
                                float(chargesMensuelles), id)
                agence.biensImmobiliers.append(a)
                working = False
                if len(agence.checkBien(a)) != 0:
                    print("TODO")

            elif type == "M":
                prix = input("Prix :")
                dateVente = input("Date de vente :")
                adresse = input("Adresse :")
                orientation = input("Orientation :")
                dateDispo = input("Disponible jusqu'au :")
                nbPiece = input("Nombre de piece")
                nbEtage = input("Etage :")
                surface = input("Surface :")
                moyenChauffage = input("Moyen de chauffage :")
                id = input("Id :")
                m = Maison(prix, dateVente, adresse, orientation, dateDispo, surface, nbPiece, nbEtage, moyenChauffage,
                           id)
                agence.biensImmobiliers.append(m)
                working = False
                if len(agence.checkBien(m)) != 0:
                    print("TODO")

            elif type == "T":
                prix = input("Prix :")
                dateVente = input("Date de vente :")
                adresse = input("Adresse :")
                orientation = input("Orientation :")
                dateDispo = input("Disponible jusqu'au :")
                surfaceSol = input("Surface au sol :")
                longueurFacade = input("Longueur de la facade :")
                id = input("Id :")
                t = Terrain(prix, dateVente, adresse, orientation, dateDispo, surfaceSol, longueurFacade, id)
                agence.biensImmobiliers.append(t)
                working = False
                if len(agence.checkBien(t)) != 0:
                    print("TODO")

            elif type == "R":
                working = False
            else:
                print("Choix invalide")

    @staticmethod
    def supprimerBien(agence, bien):
        agence.biensImmobiliers.remove(bien)
        print("Bien supprimé")
