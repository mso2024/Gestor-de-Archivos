class Permisos:
    def __init__(self,escritura,lectura):
        self.escritura = escritura
        self.lectura = lectura

    def get_escritura(self):
        return self.escritura

    def get_lectura(self):
        return self.lectura

