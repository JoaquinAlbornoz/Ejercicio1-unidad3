from manfacultad import listafacultad

def test():
    a = listafacultad()
    a.carga()
    print('----MENU----')
    x = int(input('1.Ver carreras de una Facultad.\n2.Informacion de una carrera.\nIngrese opcion: '))
    while x == 1 or x==2:
        match x:
            case 1:
                p = input('ingrese el numero de codigo: ')
                a.Mostrar(p)
            case 2:
                p = input('ingrese el nombre de la carrera: ')
                a.carrinfo(p)
        x = int(input('1.Ver carreras de una Facultad.\n2.Informacion de una carrera.\nIngrese opcion: '))
if __name__ == '__main__':
    test()