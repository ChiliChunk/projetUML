from tkinter import *
from src.Physique import Physique
import re

#Besoin de mettre l'agence dans  vérifier le format du num et de l'adresse mail
def enregistrer():
    if not re.match("[^@]+@[^@]+\.[^@]+",email.get()):
        Label(root, fg="red", text="Email Invalide").grid(column=0, row=12, sticky=(W, E))
    elif not re.match("[1-9 ]{10,15}",tel.get()):
        Label(root, fg="red", text="Telephone Invalide").grid(column=0, row=12, sticky=(W, E))
    else:
        print("ca marche")
        Label(root, fg="red", text="OK").grid(column=0, row=12, sticky=(W, E))
        user =Physique(nom.get(),adresse.get(),tel.get,email.get())
        user.inscrire()



root = Tk()
root.title("Ajout d'une personne physique")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

nom=StringVar()
adresse=StringVar()
email=StringVar()
tel=StringVar()

Label(root, text="Nom").grid(column=0, row=0 , sticky=(W, E))
Entry(root, textvariable=nom).grid(column=0, row=1, sticky=(W, E))
Label(root, text="Adresse").grid(column=0, row=3, sticky=(W, E))
Entry(root, textvariable=adresse).grid(column=0, row=4, sticky=(W, E))
Label(root, text="Mail").grid(column=0, row=6, sticky=(W, E))
Entry(root, textvariable=email).grid(column=0, row=7, sticky=(W, E))
Label(root, text="Telephone").grid(column=0, row=9, sticky=(W, E))
Entry(root, textvariable=tel).grid(column=0, row=10, sticky=(W, E))
warning = Label(root, fg="red",text="").grid(column=0, row=12, sticky=(W, E))
submit = Button(root, text="Enregistrer", command=enregistrer).grid(column=0, row=13, sticky=(W, E))
root.mainloop()

