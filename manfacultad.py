from facultad import facultad
from carrera import carrera
import csv

class listafacultad():
    def __init__(self):
        self.__listafacu = []

    def carga(self):
        with open('C:\\Users\\users\\Documents\\Cristiannika\\SEGUNDO AÑO DE FACULTAD\\Programacion orientada a objetos\\UNIDAD 3\\ejercicio1\\facultades.csv', 'r') as f:
            reader = csv.reader(f, delimiter = ';')
            facultad_actual = None
            for linea in reader:
                if linea[0].isdigit():
                    codigo = linea[0]
                    nombre = linea[1]
                    direccion = linea[2]
                    localidad = linea[3]
                    telefono = linea[4]
                    facultad_actual = facultad(codigo, nombre, direccion, localidad, telefono)
                    self.__listafacu.append(facultad_actual)
                elif facultad_actual != None:
                    codigo_facultad = facultad_actual.getcode()
                    codigo = linea[1]
                    nombre = linea[2]
                    titulo = linea[3]
                    duracion = linea[4]
                    nivel = linea[5]
                    c = carrera(codigo_facultad, codigo, nombre, titulo, duracion, nivel)
                    facultad_actual.agregarcarre(c)


    def Mostrar(self,x):
        i = 0
        t = ""
        while self.__listafacu[i] == x and i < len(self.__listafacu):
            i += 1
        if i<len(self.__listafacu):
            t = f'nombre de la facultad: {self.__listafacu[i].getnom()} carreras: '
            print (t)
            self.__listafacu[i].mostrarcarr()
            
        else:
            print('Codigo no encontrado.')

    def carrinfo(self,x):
        i = 0
        j = True
        while j and i < len(self.__listafacu):
            for carrera in self.__listafacu[i].getcarre():
                if carrera.getnom() == x:
                    print(f'codigo facultad: {self.__listafacu[i].getcode()} codigo carrera: {carrera.getcode()} nombre facultad: {self.__listafacu[i].getnom()} localidad: {self.__listafacu[i].getloc()}')
                    j = False
            i += 1