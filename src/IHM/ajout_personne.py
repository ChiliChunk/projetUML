from tkinter import *
from src.Physique import Physique
import re

class AjoutPers(Frame):

    def enregistrer(self, agence):
        if not re.fullmatch("[^@]+@[^@]+\.[^@]+",self.email.get()):
            Label(self.root, fg="red", text="Email Invalide").grid(column=0, row=12, sticky=(W, E))

        elif not re.fullmatch("[0-9]{10,15}",self.tel.get()):
            Label(self.root, fg="red", text="Telephone Invalide").grid(column=0, row=12, sticky=(W, E))
        else:
            user =Physique(self.nom.get(),self.adresse.get(),self.tel.get,self.email.get())
            user.inscrire(self.agence)

    def __init__(self, parent,agence):
        self.root = Frame.__init__(self,parent)
        parent.title("Ajout d'une personne physique")

        self.agence = agence
        self.nom=StringVar()
        self.adresse=StringVar()
        self.email=StringVar()
        self.tel=StringVar()
        Label(self.root, text="Nom").grid(column=0, row=0 , sticky=(W, E))
        Entry(self.root, textvariable=self.nom).grid(column=0, row=1, sticky=(W, E))
        Label(self.root, text="Adresse").grid(column=0, row=3, sticky=(W, E))
        Entry(self.root, textvariable=self.adresse).grid(column=0, row=4, sticky=(W, E))
        Label(self.root, text="Mail").grid(column=0, row=6, sticky=(W, E))
        Entry(self.root, textvariable=self.email).grid(column=0, row=7, sticky=(W, E))
        Label(self.root, text="Telephone").grid(column=0, row=9, sticky=(W, E))
        Entry(self.root, textvariable=self.tel).grid(column=0, row=10, sticky=(W, E))
        Label(self.root, fg="red",text="").grid(column=0, row=12, sticky=(W, E))
        Button(self.root, text="Enregistrer", command=self.enregistrer).grid(column=0, row=13, sticky=(W, E))



