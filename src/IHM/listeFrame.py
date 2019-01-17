from tkinter import *
from tkinter import ttk
from src.Agence import Agence
from src.IHM.ajout_personne import AjoutPers
from tkinter import messagebox
from src.Personne import Personne

class listeFrame(Frame):

    def __init__(self, parent):
        self.frame = Frame.__init__(self,parent)
        parent.title("Agence")

        self.agence = Agence()

        nom = []

        for personne in self.agence.personnes:
            nom += [personne.nom]

        self.cnames = StringVar(value=nom)

        self.c = ttk.Frame(self.frame, padding=(5, 5, 12, 0))
        self.c.grid(column=0, row=0, sticky=(N, W, E, S))

        self.lbox = self.tabpersonne()

        addp = ttk.Button(self.c, text='Ajout d\'une personne', command=(lambda: self.addpersonne(parent)))

        addb = ttk.Button(self.c, text="Ajout d\'un bien")

        addd = ttk.Button(self.c, text="Ajout d'une demande")

        addp.grid(column=1, row=1, sticky=(W, E))

        addd.grid(column=1, row=2, sticky=(W, E))

        addb.grid(column=1, row=3, sticky=(W, E))

        self.c.grid_columnconfigure(0, weight=1)
        self.c.grid_rowconfigure(5, weight=1)

    def tabpersonne(self):
        lbox = Listbox(self.c, listvariable=self.cnames, height=9)
        lbox.grid(column=0, row=0, rowspan=6, sticky=(N, S, E, W))
        for i in range(0, 0, 2):
            lbox.itemconfigure(i, background='#f0f0ff')
        return lbox

    def refresh(self):
        if self.lbox is not None:
            self.lbox.destroy()
        self.lbox = self.tabpersonne()

    def addpersonne(self,parent):
        if self.frame is not None:
            self.frame.destroy()

        AjoutPers(parent,self.agence)

root = Tk()

listeFrame(root)

root.mainloop()