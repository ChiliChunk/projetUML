import signal, os
import src.Model.Agence as ag
import yaml
import src.IHM.Menu as men

#A ton vraiment la visibilité de l'agence
def handlerLeave(num_sig,frame ):
    save(agence)

def save(agence):
    with open('agence.yaml','w' )as f:
        yaml.dump(agence, f)

#VERIFIER SI LES ADRESSES SONT RELATIVES AU FICHIER OU AU PROJET
def restore():
    if(os.path.isfile('./agence.yaml')):
        print("Chargement de la sauvegarde d'agence précédente")
        with open('./agence.yaml','r')as f:
            agence = yaml.load(f)
        print("Chargement de l'agence : "+agence.nom)
    else:
        print("Creation d'une nouvelle agence")
        #A ton besoin de vérifier l'input ?
        nomAgence =input("Entrez le nom de la nouvelle agence : ")
        agence = ag.Agence(nomAgence)
    return agence
if __name__ == '__main__':
    signal.signal(signal.SIGINT, handlerLeave)
    signal.signal(signal.SIGTERM,handlerLeave)
    agence = restore()
    men.Menu(agence)