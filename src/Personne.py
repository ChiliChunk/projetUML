class Personne:

    def __init__(self, nom, addresse, numTel, email, unVoeux = None):
        self.voeux = unVoeux
        self.nom = nom
        self.addresse = addresse
        self.numTel = numTel
        self.email = email

    def inscrire(self, agence):
        agence.personnes.append(self)

    def ajoutVoeux(self, voeux ):
        self.voeux = voeux
