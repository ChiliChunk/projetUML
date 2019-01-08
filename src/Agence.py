class Agence:
    def __init__(self , nom="Agence Par defaut"):
        self.rdvs = []
        self.biensImmobiliers = []
        self.annonces = []
        self.personnes = []
        self.nom = nom

    def __str__(self):
        return (f"rdvs : {''.join(str(e) for e in self.rdvs)} biens : {''.join(str(e) for e in self.biensImmobiliers)} annonces : {''.join(str(e) for e in self.annonces)} personnes : {''.join(str(e) for e in self.personnes)} NOM : {self.nom}")
    
    