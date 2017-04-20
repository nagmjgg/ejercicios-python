#programa que ejecuta sonido cada t segundos 
import pygame,time
from pygame.locals import *
 
pygame.init()

while True:

    #print "ingrese Tiempo(seg): "
    #t=int(input())

    t=220
    tiempo_duracion_musica=5
    
    for timer in range (2200):

        for event in pygame.event.get(): # event handling loop
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                
        time.sleep(1)
        print "t: %d"%(timer)

        if timer % t == 0:
            #pygame.mixer.music.load("Sonidos/aves2.mp3")
            pygame.mixer.music.load("Sonidos/laser1.mp3")
            pygame.mixer.music.play()
            time.sleep(tiempo_duracion_musica)
            pygame.mixer.music.stop()

            


    
