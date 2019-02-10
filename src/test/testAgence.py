from nose.tools import eq_, with_setup
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
        self.description = Description("Petite maison de campagne", "Article")
        self.annonce = Annonce(self.bien,self.description)
        self.voeu = Voeux(BienImmobilier.TypesBien.APPARTEMENT,500,"Paris",5)
        self.personne.ajoutVoeux(self.voeu)
        self.agence.biensImmobiliers.append(self.bien)

    @with_setup(setup)
    def testCheckVoeu(self):
        eq_(self.bien,self.agence.checkVoeux(self.voeu))

    @with_setup(setup)
    def testCheckBien(self):
         eq_(self.voeu,self.agence.checkBien(self.bien))