# -*- coding: utf-8 -*-
import pygame,sys
from pygame.locals import *
from random import randint

pygame.init() # colocar antes de cualquier modulo de pygame
ancho=600
alto=600
ventana = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("Animacion") # titulo de vnentana

Mi_imagen = pygame.image.load("imagenes/ball.bmp")

posX=200  #( numero inicial, numero final)
posY=100  # tener en cuenta que el máximo sea menor que la ventana

# entre mayor número mayor velocidad
speed=0.005
pasos=1000
print speed
Blanco=(255,255,255)
Black=(0,0,0)

derecha=True

ventana.fill(Blanco)


#pixObj[480][380] = BLACK

while True:
    #limpiar pantalla
    #ventana.fill(Blanco)

    
    #(imagen, (poxX,posY) cargar imagen
    #ventana.blit(Mi_imagen,(posX,posY))
    pygame.draw.circle(ventana, Black,(int(posX),int(posY)),2,0)
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # solución para que vaya hacía la derecha y luego hacía la izquierda

    r=randint(0,3)
    
    if r==0: #derecha
        for t in range (pasos):
            if posX<ancho:
                posX+=speed

    if r==1: #izquierda
        for t in range (pasos):
            if posX>0:
                posX-=speed

    if r==2: #abajo
        for t in range (pasos):
            if posY<alto:
                posY+=speed

    if r==3: #arriba
        for t in range (pasos):
            if posX>0:
                posY-=speed
            
    pygame.display.update() # actualizar ventana
