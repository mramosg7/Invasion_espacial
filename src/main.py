import pygame
import random
import math
from entidades.Bala import Bala
from entidades.Enemigo import Enemigo
from entidades.Jugador import Jugador

# Inicia la libreria de pygame
pygame.init()

# Creamos la pantalla de 800px por 600px
pantalla = pygame.display.set_mode((800,600))

# Titulo e icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load('./img/ovni.png')
pygame.display.set_icon(icono)

fondo = pygame.image.load('./img/Fondo.jpg')

# Puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

def mostrar_puntaje(x,y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255,255,255))
    pantalla.blit(texto, (x, y))

#Fin de juego
fuente_final = pygame.font.Font('freesansbold.ttf', 40)
def texto_final():
    mi_fuente_final = fuente_final.render(f"Juego Terminado con {puntaje} puntos", True, (255,255,255))
    pantalla.blit(mi_fuente_final, (90,250))


# Jugador
jugador1 = Jugador(368, 500,0,0,'./img/cohete.png')


# Enemigos
num_enemigos = 15
enemigos = []
for n in range(num_enemigos):
    enemigo = Enemigo(random.randint(0,736),random.randint(50, 200),0.15,50,'./img/enemigo.png')
    enemigos.append(enemigo)


# Bala
bala = Bala(0,500,0,1.5,'./img/bala.png',False)


# Detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    return distancia < 27


# Creamos un loop para que el juego este abierto hasta que el usuario cierre la ventana
se_ejecuta = True
while se_ejecuta:

    # Ajustamos el fondo
    pantalla.blit(fondo, (0,0))

    # Revisamos todos los eventos que estan succediendo en pygames
    for evento in pygame.event.get():

        # Si hay el evento de QUIT nos saldremos del bucle
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Ver si el jugador le da click a una tecla
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador1.x_cambio = -0.2

            if evento.key == pygame.K_RIGHT:
                jugador1.x_cambio = 0.2

            if evento.key == pygame.K_SPACE:
                if not bala.bala_visible:
                    bala.x = jugador1.x
                    bala.mover(pantalla)


        # Ver cuando el jugador suelta una tecla
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador1.x_cambio = 0

    # Agregamos el jugador
    jugador1.x += jugador1.x_cambio


    # Mantener dentro de bordes
    if jugador1.x <= 0:
        jugador1.x = 0
    if jugador1.x >= 736:
        jugador1.x = 736

    jugador1.mover(pantalla)


    # Movimiento bala
    if bala.y <= -64:
        bala.y = 500
        bala.bala_visible = False

    if bala.bala_visible:
        bala.mover(pantalla)
        bala.y -= bala.y_cambio



    # enemigo
    for enemigo in enemigos:

        # Fin del juego
        if enemigo.y > 490:
            for k in enemigos:
                k.y = 1000
            texto_final()
            break


        enemigo.x += enemigo.x_cambio
        if enemigo.x <= 0:
            enemigo.x_cambio = 0.15
            enemigo.y += enemigo.y_cambio
        if enemigo.x >= 736:
            enemigo.x_cambio = -0.15
            enemigo.y += enemigo.y_cambio
        enemigo.mover(pantalla)

        # Verificar colision
        colision = hay_colision(enemigo.x, enemigo.y, bala.x, bala.y)
        if colision:
            bala.y = 500
            bala.bala_visible = False
            puntaje += 100
            enemigo.x = random.randint(0, 736)
            enemigo.y = random.randint(50, 200)


    # Mostrar puntaje
    mostrar_puntaje(texto_x,texto_y)

    # Actualizar la pantalla
    pygame.display.update()