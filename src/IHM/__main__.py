import signal, os
import src.Agence as ag
import yaml
import src.IHM.menu as men

#A ton vraiment la visibilité de l'agence
def handlerLeave(num_sig,frame ):
    save(agence)

def save(agence):
    with open('./agence.yaml', )as f:
        yaml.dump(agence, f)

#VERIFIER SI LES ADRESSES SONT RELATIVES AU FICHIER OU AU PROJET
def restore():
    if(os.path.isfile('./agence.yaml')):
        print("Chargement de la sauvegarde d'Agence précéde")
        with open('./agence.yaml',)as f:
            agence = yaml.load(f)
    else:
        print("Creation d'une nouvelle agence")
        #A ton besoin de vérifier l'input ?
        nomAgence =input("Entrez le nom de la nouvelle agence : ")
        agence = ag.Agence(nomAgence)
    return agence

men.testo()
signal.signal(signal.SIGINT, handlerLeave)
signal.signal(signal.SIGTERM,handlerLeave)
agence = restore()
men.menu(agence)