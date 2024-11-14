class BDUsuarios:
    def __init__(self):
        self.usuarios=[]



    def log_in(self,correo,pwd):
        for usuario in self.usuarios:
            if usuario.correo is correo:
                if usuario.pwd is pwd:
                    return usuario
        return None

    def verif_user_exists(self,correo):
        for usuario in self.usuarios:
            if usuario.correo is correo:
                return True
        return False

    ##def create_user(self,nombre,pwd,clearance_lvl):
