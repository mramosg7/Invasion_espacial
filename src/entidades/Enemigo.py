from entidades.entidades import Entidades

class Enemigo(Entidades):
    def __init__(self, x, y, x_cambio, y_cambio, img):
        super().__init__(x, y, x_cambio, y_cambio, img)