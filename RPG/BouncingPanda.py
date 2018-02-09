import pygame, sys, random
from pygame.locals import *

FPS = 30
WINWIDTH = 640
WINHEIGHT = 480
SIZE = 80
HEROWORLDX = WINWIDTH/2
HEROWORLDY = WINHEIGHT/2
CENTER_HEROX = HEROWORLDX - SIZE/2
CENTER_HEROY = HEROWORLDY - SIZE/2
HERO_CAMX = 10
HERO_CAMY = 10
CAMX = 0
CAMY = 0
CAM_OFFSET = 90
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
         'worldX': CENTER_HEROX,
         'worldY': CENTER_HEROY}
scaledHero = pygame.transform.scale(HERO['surface'], (SIZE, SIZE))

pygame.mixer.music.load('sounds/triumph.wav') #plays the backgournd sound
pygame.mixer.music.play(-1, 0.0) #plays it forever (-1) and from the beginning (0.0)

while True:
    DISPLAYSURF.fill(BAMBOO)
    DISPLAYSURF.blit(scaledHero, (HERO_CAMX, HERO_CAMY))
    event = pygame.key.get_pressed()
        #if event.type == KEYDOWN:
    if event[pygame.K_UP] or event[pygame.K_w]:
        CENTER_HEROY -= 5
        if CENTER_HEROY < (CAMY + WINHEIGHT/2) - CAM_OFFSET:
            CAMY += CAM_OFFSET
    if event[pygame.K_LEFT] or event[pygame.K_a]:
        CENTER_HEROX -= 5
        if hero_face == 'right':
            scaledHero = pygame.transform.flip(scaledHero, True, False)
            hero_face = 'left'
        if CENTER_HEROX < (CAMX + WINWIDTH/2) - CAM_OFFSET:
            CAMX += CAM_OFFSET
    if event[pygame.K_RIGHT] or event[pygame.K_d]:
        CENTER_HEROX += 5
        if hero_face == 'left':
            scaledHero = pygame.transform.flip(scaledHero, True, False)
            hero_face = 'right'
        if CAMX >= WINWIDTH:
            CAMX = 0 - SIZE
    if event[pygame.K_DOWN] or event[pygame.K_s]:
        CENTER_HEROY += 5
        if CAMY >= WINHEIGHT:
            CAMY = 0 - SIZE
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)

