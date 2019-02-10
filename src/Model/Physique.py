from src.Model.Personne import Personne

class Physique(Personne):

    def __init__(self, nom, adresse, numTel, email):
        super().__init__()
        self.nom = nom
        self.adresse=adresse
        self.numTel =numTel
        self.email =email

    def __str__(self):
        return (f"nom : {self.nom}")
