import pygame, sys
from pygame.locals import *

FPS = 30
WINWIDTH = 400
WINHEIGHT = 300
PANDAX = 10
PANDAY = 10
SIZE = 50

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BAMBOO = (24, 255, 0)

'''
Execution of the code of the jumping panda. Pre-configuration of the game window.
'''
pygame.init()

pygame.display.set_icon(pygame.image.load('images/super_panda.png')) #Changes the icon in the task bar
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
pygame.display.set_caption('Jumping Panda')

PANDA = pygame.image.load('images/walking_panda.jpg')
scaledPanda = pygame.transform.scale(PANDA, (SIZE, SIZE))

while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(scaledPanda, (PANDAX, PANDAY))
    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key in (K_UP, K_w):
                PANDAY -= 5
            if event.key in (K_LEFT, K_a):
                PANDAX -= 5
            if event.key in (K_RIGHT, K_d):
                PANDAX += 5
            if event.key in (K_DOWN, K_s):
                PANDAY += 5

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)





pygame.quit()
