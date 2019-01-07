from src import BienImmobilier as B

class Maison(B.BienImmobilier):
    def __init__(self,prix,dateVente,adresse,orientation,dateDispo):
        super().__init__(self,prix,dateVente,adresse,orientation,dateDispo)