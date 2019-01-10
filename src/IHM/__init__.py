from tkinter import *
from tkinter import ttk
from src.Agence import Agence
from tkinter import messagebox

def addpersonne():
    messagebox.showinfo(message='Have a good day')

root = Tk()

agence = Agence()

nom = ()

for personne in agence.personnes :
    nom.__add__(personne.nom)

cnames = StringVar(value=nom)

c = ttk.Frame(root, padding=(5, 5, 12, 0))
c.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

lbox = Listbox(c, listvariable=cnames, height=9)

addp = ttk.Button(c, text='Ajout d\'une personne', command=addpersonne, default='active')

addb = ttk.Button(c, text="Ajout d\'un bien")

addd = ttk.Button(c, text="Ajout d'une demande")

lbox.grid(column=0, row=0, rowspan=6, sticky=(N,S,E,W))

addp.grid(column=1, row=1, sticky=(W,E))

addd.grid(column=1, row=2, sticky=(W,E))

addb.grid(column=1, row=3, sticky=(W,E))

c.grid_columnconfigure(0, weight=1)
c.grid_rowconfigure(5, weight=1)

for i in range(0,len(agence.personnes),2):
    lbox.itemconfigure(i, background='#f0f0ff')


root.mainloop()