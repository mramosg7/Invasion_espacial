from entidades.entidades import Entidades

class Bala(Entidades):
    def __init__(self, x, y, x_cambio, y_cambio, img, bala_visible):
        super().__init__(x, y, x_cambio, y_cambio, img)
        self.bala_visible = bala_visible

    def mover(self,pantalla):
        self.bala_visible = True
        pantalla.blit(self.img, (self.x + 16, self.y + 10))