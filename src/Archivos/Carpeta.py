class Carpeta:
    def __init__(self,nombre,padre):
        self.name = nombre
        self.padre = padre
        self.contenidos = []

    def buscar_elemento(self, nombre):
        for elemento in self.contenidos:
            if elemento.name == nombre:
                return elemento
        return None

    def verif_elemento_existe(self,nombre):
        for elemento in self.contenidos:
            if elemento.name == nombre:
                return True
        return False

    def get_nombre(self):
        return self.name

    def get_carpeta(self):
        return self.contenidos

    def eliminar_elemento(self,nombre):
        elemento_elim = self.buscar_elemento(nombre)
        if elemento_elim:
            self.contenidos.remove(elemento_elim)
            return 1
        else:
            return 0

    def agregar_elemento(self,new_element):
        if self.buscar_elemento(new_element.name) is None:
            self.contenidos.append(new_element)
            return 1
        else:
            return 0

