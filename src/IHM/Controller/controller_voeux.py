class ControllerVoeux:

    @staticmethod
    def supprimerVoeux(agence, voeu):
        for personne in agence.personnes:
            for voeux in personne.voeux:
                if voeux == voeu:
                    personne.voeux.remove(voeu)
                    print("Voeu supprimé")
