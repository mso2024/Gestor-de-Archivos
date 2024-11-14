from src.Archivos.Carpeta import Carpeta
from src.Archivos.Archivo import Archivo
from src.Navegador.Navegador import Navegador
from datetime import datetime
nav = Navegador()

nav.ver_directorio()
while True:
    print("Opciones:\n 1 - Navegar\n 2 - Volver a Home (root)\n 3 - Volver a directorio previo\n 4 - Eliminar archivo\n 5 - Agregar Archivo\n")
    opt = int(input())
    if opt == 1:
        nav.ver_directorio()
        print("Escriba el nombre de la carpeta (debe existir): ")
        nombre = str(input())
        nav.navegar(nombre)

    elif opt == 2:
        nav.ver_directorio()
        print("Escriba el nombre de la carpeta o archivo (debe existir): ")
        nombre = str(input())
        nav.current_element.eliminar_elemento(nombre)

    elif opt == 3:
        nav.ver_directorio()
        print("1 - Crear Archivo ; 2 - Crear Carpeta :")
        opt2 = int(input())
        if opt2 == 1:
            print("Introduzca el nombre del archivo: ")
            nombre = str(input())
            new_file = Archivo(datetime.now(),datetime.now(),nombre)
            nav.current_element.agregar_elemento(new_file)
            nav.ver_directorio()

        elif opt2 == 2:
            print("Introduzca el nombre de la carpeta: ")
            nombre = str(input())
            new_folder = Carpeta(nombre,nav.current_element)
            nav.current_element.agregar_elemento(new_folder)
            nav.ver_directorio()



