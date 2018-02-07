import pygame, sys
from pygame.locals import *

FPS = 30
WINWIDTH = 400
WINHEIGHT = 300
PANDAX = 10
PANDAY = 10
PIGX = 100
PIGY = 10
SIZE = 80
panda_face = 'right'
pig_face = 'right'

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

PIG = pygame.image.load('images/super_pig.png')
scaledPig = pygame.transform.scale(PIG, (SIZE, SIZE))

pygame.mixer.music.load('sounds/triumph.wav') #plays the backgournd sound
pygame.mixer.music.play(-1, 0.0) #plays it forever (-1) and from the beginning (0.0)

while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(scaledPanda, (PANDAX, PANDAY))
    DISPLAYSURF.blit(scaledPig, (PIGX, PIGY))
    event = pygame.key.get_pressed()
        #if event.type == KEYDOWN:
    if event[pygame.K_UP] or event[pygame.K_w]:
        PANDAY -= 5
        PIGY -= 5
    if event[pygame.K_LEFT] or event[pygame.K_a]:
        PANDAX -= 5
        PIGX -= 5
        if panda_face == 'right':
            scaledPig = pygame.transform.flip(scaledPig, True, False)
            scaledPanda = pygame.transform.flip(scaledPanda, True, False)
            panda_face = 'left'
            pig_face = 'left'
    if event[pygame.K_RIGHT] or event[pygame.K_d]:
        PANDAX += 5
        PIGX += 5
        if panda_face == 'left':
            scaledPig = pygame.transform.flip(scaledPig, True, False)
            scaledPanda = pygame.transform.flip(scaledPanda, True, False)
            panda_face = 'right'
            pig_face = 'right'
    if event[pygame.K_DOWN] or event[pygame.K_s]:
        PANDAY += 5
        PIGY += 5

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)





pygame.quit()
