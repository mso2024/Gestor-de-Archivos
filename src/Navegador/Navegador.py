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


    def navegar(self, nombre_elemento, auth_token):
        if auth_token is True:
            temp_element = None
            if self.current_element.verif_elemento_existe(nombre_elemento):
                temp_element = self.current_element.buscar_elemento(nombre_elemento)
                self.current_element = temp_element
                self.ruta = self.ruta + "/" + self.current_element.get_nombre() + "/"
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
        self.ruta = self.ruta.rsplit("/",1)[0]
        self.current_element = temp_element



