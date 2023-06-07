

class facultad():
    def __init__(self,code, nom, dire, loc, tel):
        self.__code = code
        self.__nom = nom
        self.__dire = dire
        self.__loc = loc
        self.__tel = tel
        self.__carre = []
    
    def __del__(self):
        for c in self.__carre:
            del c
        print('Facultad y sus carreras eliminadas')
    
    def agregarcarre(self, carre):
        self.__carre.append(carre)

    def getcode(self):
        return self.__code

    def getnom(self):
        return self.__nom

    def getdire(self):
        return self.__dire

    def getloc(self):
        return self.__loc

    def gettel(self):
        return self.__tel

    def getcarre(self):
        return self.__carre
    
    def mostrarcarr(self):
        for c in self.__carre:
            print(f'{c.getnom()}, {c.getdur()} Años')

    def __eq__(self, other):
        if type(other)==type(self):
            return self.getcode() == other.getcode()
        else: 
            return self.getcode()==other