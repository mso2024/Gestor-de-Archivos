from src.Archivos.Carpeta import Carpeta
from src.Navegador.Autenticador import Autenticador
from src.Usuarios.Usuario import Usuario
class Navegador:
    def __init__(self):
        self.contenidos = Carpeta("home",None,0)
        self.contenidos.agregar_elemento(Carpeta("Documentos",self.contenidos,0))
        self.contenidos.agregar_elemento(Carpeta("Videos",self.contenidos,0))
        self.current_element = self.contenidos
        self.ruta = "/home"
        self.autenticador = Autenticador()

    def ver_directorio(self):
        print("Gestor de Archivos PyCharm\nRuta: " + self.ruta + "\n")
        for element in self.current_element.contenidos:
            if isinstance(element, Carpeta):
                print("Carpeta: " + element.get_nombre() + "\n")
            else:
                print("Archivo: " + element.get_nombre() + "\n")

    def reconstruir_ruta(self):
        ruta = []
        temp = self.current_element
        while temp is not None:
            ruta.append(temp.get_nombre())  # Add folder name to the path
            temp = temp.padre  # Move to the parent folder
        return "/" + "/".join(reversed(ruta))  # Join names in reverse to get the correct path

    def navegar(self, nombre_elemento, auth_token):
        if auth_token == True:
            temp_element = None
            if self.current_element.verif_elemento_existe(nombre_elemento):
                self.ver_directorio()
                temp_element = self.current_element.buscar_elemento(nombre_elemento)
                self.current_element = temp_element
                prev_ruta = self.ruta
                self.ruta = prev_ruta + "/" + self.current_element.get_nombre() + "/"
                return 1
            else:
                print("La carpeta no existe, por favor intentelo de nuevo\n")
                return 0

        print("No tiene permiso para ver este elemento.")

    def go_home(self):
        self.current_element = self.contenidos
        self.ruta = "/home"

    def go_back(self):
        temp_element = self.current_element.padre
        if temp_element is not None:
            self.current_element = temp_element
            self.ruta = self.reconstruir_ruta()
        else:
            print("Ya está en el directorio raíz.")

    def mover_elemento(self, nombre_elemento, nombre_destino, user_clearance_lvl):
        if not self.autenticador.autenticar_cv_elemento(user_clearance_lvl):
            print("No tiene permiso para mover elementos.")
            return 0
        elemento = self.current_element.buscar_elemento(nombre_elemento)
        if not elemento:
            print(f"El elemento '{nombre_elemento}' no existe en el directorio actual.")
            return 0
        destino = self.current_element.buscar_elemento(nombre_destino)
        if not isinstance(destino, Carpeta):
            print(f"El destino '{nombre_destino}' no es una carpeta válida.")
            return 0
        self.current_element.eliminar_elemento(nombre_elemento)
        if destino.agregar_elemento(elemento):
            elemento.padre = destino
            print(f"El elemento '{nombre_elemento}' se ha movido a la carpeta '{nombre_destino}'.")
            return 1
        else:
            self.current_element.agregar_elemento(elemento)
            print(
                f"No se pudo mover el elemento '{nombre_elemento}' a '{nombre_destino}'. Ya existe un elemento con el mismo nombre.")
            return 0


