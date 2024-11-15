from src.Usuarios.Usuario import Usuario


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

    def get_user(self,correo):
        for usuario in self.usuarios:
            if usuario.correo is correo:
                return usuario
        return None

    def create_user(self,nombre,pwd,clearance_lvl,correo):
        new_user = Usuario(nombre,correo,clearance_lvl,pwd)
        self.usuarios.append(new_user)


    def modify_user_name(self,correo,new_name):
        for user in self.usuarios:
            if user.correo is correo:
                user.name = new_name
                return 1
        return 0

    def modify_user_mail(self,correo,new_mail):
        for user in self.usuarios:
            if user.correo is correo:
                user.correo = new_mail
                return 1
        return 0

    def modify_user_clearance(self,correo,new_clearance_lvl):
        for user in self.usuarios:
            if user.correo is correo:
                user.clearance_lvl = new_clearance_lvl
                return 1
        return 0



    def delete_user(self,correo):
        elim_user = self.get_user(correo)
        if elim_user:
            self.usuarios.remove(elim_user)
            return 1
        else:
            return 0


