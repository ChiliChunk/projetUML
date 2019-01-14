from tkinter import *
from src.Physique import Physique
import re
import datetime
import time
root = Tk()
root.title("Choix date")



root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

date = StringVar(value='jj/mm/aaaa')
heure = StringVar(value='00hmm')

Label(root, text="Jour").grid()

Combobox(root, textvariable=date).grid()
Label(root, text="Heure").grid()
Entry(root,textvariable=heure).grid()




root.mainloop()