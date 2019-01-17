from src.Personne import Personne

class Physique(Personne):

    def __init__(self, nom, addresse, numTel, email):
        super().__init__()
        self.nom = nom
        self.addresse = addresse
        self.numTel = numTel
        self.email = email

    def __str__(self):
        return (f"nom : {self.nom}")