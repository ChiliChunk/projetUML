from nose.tools import eq_, with_setup, assert_false, assert_true
from src.Model.Agence import Agence
from src.Model.Annonce import Annonce
from src.Model.Appartement import Appartement
from src.Model.BienImmobilier import BienImmobilier
from src.Model.Description import Description
from src.Model.Physique import Physique
from src.Model.Voeux import Voeux


class testPersonne:
    def setup(self):
        self.agence = Agence()

        self.personne = Physique("Pierre Dufour","12 impasse de la cheminée", "0782546512","toto@gmail.com")
        self.voeu = Voeux(BienImmobilier.TypesBien.APPARTEMENT, 500, "Paris", 5)
        self.personne.ajoutVoeux(self.voeu)

    @with_setup(setup)
    def testInscrire(self):
        assert_false(self.agence.personnes.__contains__(self.personne))
        self.personne.inscrire(self.agence)
        assert_true(self.agence.personnes.__contains__(self.personne))

    @with_setup(setup)
    def testAjoutVoeux(self):
        assert_false(self.personne.voeu.__contains__(self.voeu))
        self.personne.ajoutVoeux(self.voeu)
        assert_true(self.personne.voeu.__contains__(self.voeu))
