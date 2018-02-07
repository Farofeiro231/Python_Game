import pygame
import time

pygame.init()
soundObj = pygame.mixer.Sound('noo.mp3')
soundObj.play()
time.sleep(1.5)
soundObj.stop()
