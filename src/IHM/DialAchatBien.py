from tkinter import *
from src.Physique import Physique
from src.Voeux import Voeux
from src.BienImmobilier import BienImmobilier
import re

class DialAchatBien:

    def __init__(self , personne):
        frame = Tk()
        self.master = frame
        self.localisation = StringVar()
        self.nbPiece = StringVar()
        self.prix = StringVar()
        self.surface = StringVar()
        self.typeSelected = ''
        self.personne = personne
        self.errorLabel = Label(frame , text=None)
        print(self.errorLabel)

    def update(self):
        for widget in self.master.winfo_children():
            if widget.grid_info().get('row') != None:
                if widget.grid_info().get('row') >= 4:
                    widget.destroy()

    def renderFields(self):

        self.update()

        Label(self.master, text="Prix souhaité").grid(row=2)
        entryPrix = Entry(self.master , textvariable=self.prix)
        entryPrix.grid(row=2, column=1)
        Label(self.master, text="Localisation").grid(row=3)
        entryLocalisation = Entry(self.master , textvariable=self.localisation)
        entryLocalisation.grid(row=3, column=1)
        if typeSelected == "Appartement":
            labNbPiece = Label(self.master, text="Nombre de piece").grid(row=4)
            entryNbPice = Entry(self.master , textvariable=self.nbPiece)
            entryNbPice.grid(row=4, column=1)

        if typeSelected == "Terrain":
            labSurface = Label(self.master, text="Surface (m²)").grid(row=4)
            entrySurface = Entry(self.master , textvariable=self.surface)
            entrySurface.grid(row=4, column=1)

        if typeSelected == "Maison":
            labNbPiece =  Label(self.master, text="Nombre de piece").grid(row=4)
            entrySurface = Label(self.master, text="Surface (m²)").grid(row=5)
            entryNbPice = Entry(self.master , textvariable=self.nbPiece)
            entrySurface = Entry(self.master , textvariable=self.surface)
            entryNbPice.grid(row=4, column=1)
            entrySurface.grid(row=5, column=1)

        submit = Button(self.master , text = "Enregistrer" ,command=self.submitHandler).grid(row="6")

    def submitHandler(self):
        self.errorLabel['test'] = 'TEST'
        self.errorLabel.grid(row="7")
        if typeSelected == 'Appartement':
            if re.fullmatch('[0-9]*' , self.prix.get()) and re.fullmatch('[0-9]*' , self.nbPiece.get()):
                voeux = Voeux (BienImmobilier.TypesBien.APPARTEMENT,int(self.prix.get()),self.localisation,int(self.nbPiece.get()))
                self.personne.ajoutVoeux(voeux)
            else:
                ...
        elif typeSelected == 'Maison':
            voeux = Voeux (BienImmobilier.TypesBien.MAISON,int(self.prix.get()),self.localisation.get(),int(self.nbPiece.get()) , int(self.surface.get()))
            self.personne.ajoutVoeux(voeux)

        elif typeSelected == 'Terrain':
            voeux = Voeux (BienImmobilier.TypesBien.TERRAIN,int(self.prix.get()),self.localisation.get(),int(self.surface.get()))
            self.personne.ajoutVoeux(voeux)

        print(self.localisation.get())
        print(self.nbPiece.get())
        print(self.prix.get())
        print(self.surface.get())


    def changeHandler(self,event):
        global typeSelected
        typeSelected = event
        self.renderFields()

    def renderDropdownMenu(self):
        variable = StringVar (self.master)
        variable.set("Choose")  # default value
        OptionMenu(self.master, variable, "Appartement", "Terrain", "Maison", command=self.changeHandler).grid(row=1, column="1")


    def render(self):

        Label(self.master, text="Entrer un voeux d'achat").grid(row=0 , sticky=(E,W))
        self.master.title("Ajout d'un voeux")
        self.renderDropdownMenu()
        mainloop( )


phys = Physique('test','add' , 'numTel' , 'email')
frame = DialAchatBien(phys)
frame.render()