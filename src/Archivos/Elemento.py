class Elemento:
    def __init__(self,nombre,c_date,m_date):
        self.nombre = nombre
        self.c_date = c_date
        self.m_date = m_date

    def cambiar_nombre(self, new_name):
        self.nombre = new_name

    def get_nombre(self):
        return self.nombre

