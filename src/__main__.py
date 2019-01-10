from src.Physique import Physique
from src.Agence import Agence

personne = Physique('nom', 'addresse', 'numTel', 'email' )
agence = Agence()
personne.inscrire(agence)
print(personne)
print(agence)