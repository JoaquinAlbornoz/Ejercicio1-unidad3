class carrera():
    def __init__(self, codefacu, code, nom, fecha, dur, titulo):
        self.__codefacu = codefacu
        self.__code = code
        self.__nom = nom
        self.__fecha = fecha
        self.__dur = dur
        self.__titulo = titulo

    def getnom(self):
        return self.__nom

    def getdur(self):
        return self.__dur

    def getcode(self):
        return self.__code

