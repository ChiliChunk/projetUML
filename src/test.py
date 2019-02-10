class test:
    def __init__(self,a):
        self.a = a+4
        self.testo()
    def testo(self):
        return ("COucou"+ str(self.a))

print( test(15))