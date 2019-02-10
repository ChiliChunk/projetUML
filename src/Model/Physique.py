from src.Model.Personne import Personne

class Physique(Personne):

    def __init__(self, nom, addresse, numTel, email):
        super().__init__()
        self.nom = nom
        self.adresse = addresse
        self.numTel = numTel
        self.email = email

    def __str__(self):
        return (f"nom : {self.nom}")
