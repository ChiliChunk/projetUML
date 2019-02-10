class Annonce:
    def __init__(self, bien, description):
        self.medias = []
        self.bien = bien
        self.description = description

    def ajouter(self, agence):
        agence.annonces += [self]
