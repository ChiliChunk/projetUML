import yaml
import os
from src.Agence import Agence
from src.IHM.Controller.controller_bien import ControllerBien
from src.IHM.Controller.controller_client import ControllerClient


class MainController:
    def __init__(self):
        self.agence = Agence()

    def start(self):
        self.agence = self.load()
        self.menu()
        self.save(self.agence)

    def load(self):
        if os.path.exists("agence.dat"):
            with open("agence.dat", 'r') as f:
                return yaml.load(f)
        return self.agence

    def save(self, agence):
        if os.path.exists("agence.dat"):
            storeddata = self.load()
            if storeddata != agence:
                with open("agence.dat", 'w') as f:
                    yaml.dump(agence, f)
        else:
            with open("agence.dat", 'w') as f:
                yaml.dump(agence, f)

    def menu(self):
        working = True
        while working:
            choix = input("Bienvenue :"
                          "     C: Liste des clients\n"
                          "     A: Ajouter un client\n"
                          "     R: Liste des rendez-vous\n"
                          "     B: Liste des biens\n"
                          "     Q: Quitter\n")

            if choix == "C":
                ControllerClient.menu(self.agence)
            elif choix == "A":
                ControllerClient.ajouterClient(self.agence)
            elif choix == "R":
                ControllerRendezVous.menu(self.agence)
            elif choix == "B":
                ControllerBien.menu(self.agence)
            elif choix == "Q":
                working = False
            else:
                print("Choix non valide")
