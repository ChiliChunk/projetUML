from src.Model.Personne import Personne

class Physique(Personne):

    def __init__(self, nom, addresse, numTel, email):
        super().__init__(nom, addresse, numTel, email)

    def __str__(self):
        return (f"nom : {self.nom}")
