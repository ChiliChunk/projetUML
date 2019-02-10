import re
import src.Physique as prs
import src.IHM.Menu as men
regXmail ="[^@]+@[^@]+\.[^@]+"
regXTel ="[0-9]{10,15}"

class ctrlAjoutPersonne:

    def __init__(self, agence):
        self.agence = agence
    def validateInputMail(self, input ):
        return re.fullmatch(regXmail, input)
    def validateInputTel(selfself, input):
        return re.fullmatch(regXTel, input)
    def ajoutPers(self,nom,adresse,tel,adresseMail):
        pers = prs.Personne(nom, adresse, tel, adresseMail)
        pers.inscrire(self.agence)
    def redirection(self):
        men.Menu(self.agence)