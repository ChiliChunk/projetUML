from src import Personne

class Physique(Personne):

    def __init__(self, nom, addresse, numTel, email):
        super().__init__()
        self.nom = nom
        self.addresse = addresse
        self.numTel = numTel
        self.email = email