class Archivo:
    def __init__(self, c_date,m_date,name):
        self.c_date = c_date
        self.m_date = m_date
        self.name = name
        self.extension = name.split(".")[-1]

    def cambiar_nombre(self,new_name):
        self.name = new_name

    def get_nombre(self):
        return self.name



