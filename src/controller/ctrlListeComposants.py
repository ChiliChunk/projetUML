from enum import Enum
import re
import src.IHM.Menu as men
regXnbCompo = "[0-9]+"

class ctrlListeComposants:
    def __init__(self, agence, type, personne=None):
        self.agence = agence
        if type == typeCompo.PERSONNE:
            self.compos = agence.personnes
        elif type == typeCompo.BIEN:
            if personne:
                self.compos = []
                for bien in agence.biensImmobiliers:
                    if personne:
                        if bien.vendeur == personne:
                            self.compos.append(bien)
            else:
                self.compos=agence.biensImmobiliers
        elif type == typeCompo.RDV :
            self.compos = agence.rdvs
        elif type== typeCompo.ANNONCE.value:
            self.compos = agence.annonces
        else:
            raise Exception

    def validateInputChoice(self, choice):
        return (not re.fullmatch(regXnbCompo, choice)==None) and int(choice)<=len(self.compos)

    def submitChoice(self, choice):
        if choice == "0":
            men.Menu(self.agence)
        else:
            return self.compos[int(choice)-1]

class typeCompo(Enum):
    PERSONNE =1
    BIEN =2
    RDV=3
    ANNONCE = 4
