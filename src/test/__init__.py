from nose.tools import eq_, with_setup
from src.Model.Agence import Agence

class testAgence:
    def setup(self):
        self.agence = Agence()
