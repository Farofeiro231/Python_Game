import pygame, sys, random
from pygame.locals import *

FPS = 30
WINWIDTH = 640
WINHEIGHT = 480
HEROWORLDX = 10
HEROWORLDY = 10
HERO_CAMX = 10
HERO_CAMY = 10
CAMX = 0
CAMY = 0
CAM_OFFSET = 90
SIZE = 80
hero_face = 'right'

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BAMBOO = (24, 255, 0)

'''
Execution of the code of the jumping hero. Pre-configuration of the game window.
'''
pygame.init()

pygame.display.set_icon(pygame.image.load('images/super_panda.png')) #Changes the icon in the task bar
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
pygame.display.set_caption('Jumping Hero')

HERO = {'surface': pygame.image.load('images/hero.png'),
         'worldX': HEROWORLDX,
         'worldY': HEROWORLDY}
scaledHero = pygame.transform.scale(HERO['surface'], (SIZE, SIZE))

pygame.mixer.music.load('sounds/triumph.wav') #plays the backgournd sound
pygame.mixer.music.play(-1, 0.0) #plays it forever (-1) and from the beginning (0.0)

while True:
    HERO_CAMX = HEROWORLDX - CAMX
    HERO_CAMY = HEROWORLDY - CAMY
    DISPLAYSURF.fill(BAMBOO)
    DISPLAYSURF.blit(scaledHero, (HERO_CAMX, HERO_CAMY))
    event = pygame.key.get_pressed()
        #if event.type == KEYDOWN:
    if event[pygame.K_UP] or event[pygame.K_w]:
        HEROWORLDY -= 5
        CAMY -= 5
        if CAMY <= -SIZE:
            CAMY = WINHEIGHT
    if event[pygame.K_LEFT] or event[pygame.K_a]:
        HEROWORLDX -= 5
        CAMX -= 5
        if hero_face == 'right':
            scaledHero = pygame.transform.flip(scaledHero, True, False)
            hero_face = 'left'
        if CAMX <= -SIZE:
            CAMX = WINWIDTH
    if event[pygame.K_RIGHT] or event[pygame.K_d]:
        HEROWORLDX += 5
        CAMX += 5
        if hero_face == 'left':
            scaledHero = pygame.transform.flip(scaledHero, True, False)
            hero_face = 'right'
        if CAMX >= WINWIDTH:
            CAMX = 0 - SIZE
    if event[pygame.K_DOWN] or event[pygame.K_s]:
        HEROWORLDY += 5
        CAMY += 5
        if CAMY >= WINHEIGHT:
            CAMY = 0 - SIZE
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)

