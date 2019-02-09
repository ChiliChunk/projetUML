import re

regXchoice = "[123]"


class ctrlMenu:
    def __init__(self,agence):
        self.agence =agence

    def validateInputChoice(choice):
        return re.fullmatch(choice)
    def chooseOption(self,choice):
        if choice == "1":
           ...
        elif choice == "2":
            ...
        elif choice == "3":
            print("Not implemented yet")
