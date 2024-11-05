class Putns():
    def __init__(self, krasa,vide,lido):
        self.krasa = krasa
        self.vide = vide
        self.lido = bool(lido) # boll pārveido mainīgo no datu tipu boolen (true and false)

zvirbulis = Putns("pelēka","pļava",True)   
print(zvirbulis.krasa)
print(zvirbulis.vide)
print(zvirbulis.lido)     


