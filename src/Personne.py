class Personne:

    def __init__(self ,unVoeux = None):
        self.voeux = unVoeux

    def inscrire(self, agence):
        agence.personnes.append(self)