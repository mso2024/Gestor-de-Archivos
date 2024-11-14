class Autenticador:
    def autenticar_cv_elemento(self,clearance_lvl):
        if clearance_lvl >= 2:
            return True
        return False

    def autenticar_cem_usuario(self,clearance_lvl):
        if clearance_lvl is 3:
            return True
        return False

