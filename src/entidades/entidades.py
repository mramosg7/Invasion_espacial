import pygame
class Entidades():

    def __init__(self,x,y,x_cambio,y_cambio, img):
        self.x = x
        self.y = y
        self.x_cambio = x_cambio
        self.y_cambio = y_cambio
        self.img = pygame.image.load(img)

    def mover(self,pantalla):
        pantalla.blit(self.img, (self.x, self.y))