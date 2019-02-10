from nose.tools import eq_, with_setup, assert_false, assert_true
from src.Model.Agence import Agence
from src.Model.Annonce import Annonce
from src.Model.Appartement import Appartement
from src.Model.BienImmobilier import BienImmobilier
from src.Model.Description import Description
from src.Model.Physique import Physique
from src.Model.Voeux import Voeux


class testAgence:
    def setup(self):
        self.agence = Agence()

        self.personne = Physique("Pierre Dufour","12 impasse de la cheminée", "0782546512","toto@gmail.com")
        self.personne.inscrire(self.agence)
        self.bien = Appartement(200, None,"3 rue de la capucine","Nord","12/04/2019",self.personne,5,1,15000)

    @with_setup(setup)
    def testInscrire(self):
        assert_false(self.agence.biensImmobiliers.__contains__(self.bien))
        self.bien.inscrire(self.agence)
        assert_true(self.agence.biensImmobiliers.__contains__(self.bien))