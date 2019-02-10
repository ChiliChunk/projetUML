from enum import Enum
import re
from src.IHM.Menu import Menu
regXnbCompo = "[0-9]+"

class ctrlListeComposants:
    def __init__(self, agence, type, personne=None):
            if type == typeCompo.PERSONNE:
                self.compos = agence.personnes
            elif type == typeCompo.BIEN:
                self.compos = []
                for bien in agence.biensImmobiliers:
                    if bien.vendeur == personne:
                        self.compos.append(bien)
            elif type == typeCompo.RDV :
                self.compos = agence.rdvs

    def validateInputChoice(self, choice):
        return (not re.fullmatch(regXnbCompo, choice)==None) and int(choice)<len(self.compos)

    def submitChoice(self, choice):
        if choice == "0":
            Menu(self.agence)
        else:
            return self.compos[choice-1]

class typeCompo(Enum):
    PERSONNE =1
    BIEN =2
    RDV=3