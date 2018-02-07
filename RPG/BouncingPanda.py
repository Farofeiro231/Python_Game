import pygame, sys
from pygame.locals import *

FPS = 30
WINWIDTH = 1280
WINHEIGHT = 720

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BAMBOO = (24, 255, 0)

'''
Execution of the code of the jumping panda
'''
pygame.init()
pygame.display.set_icon(pygame.image.load('super_panda.png')) #Changes the icon in the task bar
DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption('Jumping Panda')
pygame.display.update()

pygame.quit()
