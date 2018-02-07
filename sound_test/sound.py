import pygame, sys
from pygame.locals import *
import time

pygame.init()
soundObj = pygame.mixer.Sound('beep-01a.wav')
soundObj.play()
time.sleep(0.5)
soundObj.stop()
