from tkinter import *

master = Tk()

def update():
    for widget in master.winfo_children():
        if widget.grid_info().get('row') >= 4:
            widget.destroy()

def renderFields(typeSelected):

    update()

    Label(master, text="Prix souhaité").grid(row=2)
    entryPrix = Entry(master)
    entryPrix.grid(row=2, column=1)
    Label(master, text="Localisation").grid(row=3)
    entryLocalisation = Entry(master)
    entryLocalisation.grid(row=3, column=1)
    if typeSelected == "Appartement":
        labNbPiece = Label(master, text="Nombre de piece").grid(row=4)
        entryNbPice = Entry(master)
        entryNbPice.grid(row=4, column=1)

    if typeSelected == "Terrain":
        labSurface = Label(master, text="Surface (m²)").grid(row=4)
        entrySurface = Entry(master)
        entrySurface.grid(row=4, column=1)

    if typeSelected == "Maison":
        labNbPiece =  Label(master, text="Nombre de piece").grid(row=4)
        entrySurface = Label(master, text="Surface (m²)").grid(row=5)
        entryNbPice = Entry(master)
        entrySurface = Entry(master)
        entryNbPice.grid(row=4, column=1)
        entrySurface.grid(row=5, column=1)


def changeHandler(event):
    renderFields(event)

def renderDropdownMenu(master):
    variable = StringVar(master)
    variable.set("Appartement")  # default value
    OptionMenu(master, variable, "Appartement", "Terrain", "Maison", command=changeHandler).grid(row=1, column="1")


def renderDialAchatBien():

    Label(master, text="Entrer un voeux d'achat").grid(row=0)
    renderDropdownMenu(master)
    mainloop( )

renderDialAchatBien()