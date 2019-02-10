class Personne:

    def __init__(self, nom, addresse, numTel, email):
        self.nom = nom
        self.addresse = addresse
        self.numTel = numTel
        self.email = email

    def inscrire(self, agence):
        agence.personnes.append(self)

    def ajoutVoeux(self, voeux ):
        self.voeux = voeux

    def afficherNom(self):
        print(self.nom)

    def __str__(self):
        return self.nom