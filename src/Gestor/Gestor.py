from src.Archivos.Carpeta import Carpeta
from src.Archivos.Archivo import Archivo
from src.Navegador.Autenticador import Autenticador
from src.Navegador.Navegador import Navegador
from datetime import datetime
from src.Usuarios.BDUsuarios import BDUsuarios
nav = Navegador()
bd = BDUsuarios()
autenticador = Autenticador()


while True:
    print("Por Favor introduzca su correo y contraseña (en ese orden): ")
    correo = str(input())
    pwd = str(input())
    global_user = None
    if bd.verif_user_exists(correo):
        global_user = bd.log_in(correo,pwd)
        break
    else:
        print("El usuario no existe, por favor intentelo de nuevo")

while True:
    if global_user.clearance_lvl is 3:
        print("Opciones:\n 1 - Navegar\n 2 - Volver a Home (root)\n 3 - Volver a directorio previo\n 4 - Eliminar elemento\n 5 - Agregar elemento\n 6 - Modificar Usuario\n 7 - Eliminar Usuario\n 8 - Modificar Usuario\n")
    elif global_user.clearance_lvl is 2:
        print("Opciones:\n 1 - Navegar\n 2 - Volver a Home (root)\n 3 - Volver a directorio previo\n 4 - Eliminar elemento\n 5 - Agregar elemento\n")
    elif global_user.clearance_lvl is 1:
        print( "Opciones:\n 1 - Navegar\n 2 - Volver a Home (root)\n 3 - Volver a directorio previo\n")

    opt = int(input())
    if opt == 1:
        nav.ver_directorio()
        print("Escriba el nombre de la carpeta (debe existir): ")
        nombre = str(input())
        nav.navegar(nombre,autenticador.autenticar_cv_elemento(global_user.clearance_lvl))
    elif opt == 2:
        nav.go_home()
        nav.ver_directorio()
    elif opt == 3:
        nav.go_back()
        nav.ver_directorio()
    elif opt == 4:
        if autenticador.autenticar_cv_elemento(global_user.clearance_lvl):
            nav.ver_directorio()
            print("Escriba el nombre de la carpeta o archivo (debe existir): ")
            nombre = str(input())
            nav.current_element.eliminar_elemento(nombre)
        else:
            print("No tiene permiso para hacer esto.")
    elif opt == 5:
        if autenticador.autenticar_cv_elemento(global_user.clearance_lvl):
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
        else:
            print("No tiene permiso para hacer esto.")
    elif opt == 6:
        if autenticador.autenticar_cem_usuario(global_user.clearance_lvl):
            print("Introduzca el correo del usuario : ")
            correo = str(input())
            if bd.verif_user_exists(correo):
                opt3 = int(input("1 - Modificar correo\n2 - Modificar Nombre\n3 - Modificar Permisos\n"))
                if opt3 is 1:
                    new_mail = str(input("Introduzca el nuevo correo: "))
                    if bd.modify_user_mail(correo,new_mail):
                        print("Nombre modificado exitosamente.")
                    else:
                        print("Error modificando el correo.")
                elif opt3 is 2:
                    new_name = str(input("Introduzca el nuevo nombre: "))
                    if bd.modify_user_name(correo, new_name):
                        print("Nombre modificado exitosamente.")
                    else:
                        print("Error modificando el nombre.")
                elif opt3 is 3:
                    new_clearance_lvl = str(input("Nuevo nivel de nivel de autorización (1=Consultor,2=Director de proyecto,3=Administrador): "))
                    if bd.modify_user_clearance(correo,new_clearance_lvl):
                        print("Autorización cambiada exitosamente.")
                    else:
                        print("Error cambiando autorización.")


            else:
                print("El usuario no existe, por favor intentelo de nuevo.")
        else:
            print("No tiene permiso para hacer esto.")
    elif opt == 7:
        if autenticador.autenticar_cem_usuario(global_user.clearance_lvl):
            print("Introduzca el correo del usuario que desea eliminar: ")
            correo = str(input())
            if bd.verif_user_exists(correo):
                if bd.delete_user(correo) is 1:
                    print("Usuario eliminado exitosamente.")
                else:
                    print("Error eliminando el usuario.")
            else:
                print("El usuario no existe.")

        else:
            print("No tiene permiso para hacer esto.")
    elif opt == 8:
        if autenticador.autenticar_cem_usuario(global_user.clearance_lvl):
            nombre = str(input("Introduzca el nombre del nuevo usuario: "))
            correo = str(input("Introduzca el correo del nuevo usuario: "))
            pwd = str(input("Introduzca la contraseña del usuario: "))
            clearance_lvl = str(input("Introduzca el nivel de autorización (1=Consultor,2=Director de proyecto,3=Administrador):"))
            bd.create_user(nombre,pwd,clearance_lvl,correo)
            print("Usuario creado con exito.")

        else:
            print("No tiene permiso para hacer esto.")