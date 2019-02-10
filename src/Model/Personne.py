class Personne:

    def __init__(self, unVoeux = None):
        self.voeux = unVoeux

    def inscrire(self, agence):
        agence.personnes.append(self)

    def ajoutVoeux(self, voeux ):
        self.voeux = voeux

    def afficherNom(self):
        print(self.nom)

    def __str__(self):
        return self.nom