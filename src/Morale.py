from src import Personne

class Morale(Personne):

    def __init__(self, numSiren, formeJuridique):
        super().__init__()
        self.numSiren = numSiren
        self.formeJuridique = formeJuridique