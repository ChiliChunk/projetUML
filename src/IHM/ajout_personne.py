from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Ajout d'une personne")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

nom = StringVar()

nom_entry = ttk.Entry(mainframe, width=7, textvariable=nom)
nom_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, text="Nom :").grid(column="")

root.mainloop()