from tkinter import *
from src.Date import Date
class choixRDV(Frame):

    def enregistrer(self,jour,heure):
        return Date(jour, heure)

    def __init__(self, parent):
        self.root = Frame.__init__(self, parent)
        parent.title("Ajout d'une personne physique")
        jour = StringVar(value='jj/mm/aaaa')
        heure = StringVar(value='12h00')
        Label(self.root, text="Jour").grid()
        Entry(self.root, textvariable=jour).grid()
        Label(self.root, text="Heure").grid()
        Entry(self.root,textvariable=heure).grid()
        Button(self.root, text="Enregistrer", command=(lambda:self.enregistrer(jour,heure))).grid()



