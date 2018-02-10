import pygame, sys, random
from pygame.locals import *

FPS = 30
WINWIDTH = 640
WINHEIGHT = 480
HALF_WINWIDHT = int(WINWIDTH/2)
HALF_WINHEIGHT = int(WINHEIGHT/2)
SIZE = 80
CAM_OFFSET = 90
RIGHT = 'right'
LEFT = 'left'

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BAMBOO = (24, 255, 0)

'''
Execution of the code of the jumping hero. Pre-configuration of the game window.
'''

def main():
    global FPSCLOCK, R_HERO, L_HERO, DISPLAYSURF
    pygame.init()

    pygame.display.set_icon(pygame.image.load('images/super_panda.png')) #Changes the icon in the task bar
    FPSCLOCK = pygame.time.Clock()

    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    pygame.display.set_caption('Jumping Hero')

    R_HERO = pygame.image.load('images/hero.png')
    L_HERO = pygame.transform.flip(R_HERO, True, False)


    while True:
        runGame()


def runGame():

    hero = {'surface': pygame.transform.scale(R_HERO, (SIZE, SIZE)),
         'x': HALF_WINWIDHT,
         'y': HALF_WINHEIGHT,
         'size': SIZE,
         'facing': RIGHT}

    camerax = 0
    cameray = 0
#scaledHero = pygame.transform.scale(hero['surface'], (hero['size'], hero['size']))

#pygame.mixer.music.load('sounds/triumph.wav') #plays the backgournd sound
#pygame.mixer.music.play(-1, 0.0) #plays it forever (-1) and from the beginning (0.0)

    while True:

        '''The coordinates system is similar to any other used with multiple referentials.
         First we subtract the world player's position from the world camera's position, then we 
         obtain the player position in the camera referential.'''
        hero['rect'] = pygame.Rect(hero['x'] - camerax,
                                   hero['y'] - cameray,
                                   hero['size'],
                                   hero['size'])

        DISPLAYSURF.fill(BAMBOO)
        DISPLAYSURF.blit(hero['surface'], hero['rect'])
        event = pygame.key.get_pressed()
            #if event.type == KEYDOWN:
        if event[pygame.K_UP] or event[pygame.K_w]:
            hero['y'] -= 5
        if event[pygame.K_LEFT] or event[pygame.K_a]:
            hero['x'] -= 5
            if hero['facing'] == RIGHT:
                hero['surface'] = pygame.transform.scale(L_HERO, (hero['size'], hero['size']))
                hero['facing'] = LEFT
        if event[pygame.K_RIGHT] or event[pygame.K_d]:
            hero['x'] += 5
            if hero['facing'] == LEFT:
                hero['surface'] = pygame.transform.scale(R_HERO, (hero['size'], hero['size']))
                hero['facing'] = RIGHT
        if event[pygame.K_DOWN] or event[pygame.K_s]:
            hero['y'] += 5

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()

        heroCenterx = hero['x'] + int(hero['size']/2)
        heroCentery = hero['y'] + int(hero['size']/2)

        if (camerax + HALF_WINWIDHT) - heroCenterx > CAM_OFFSET:
            camerax = heroCenterx + CAM_OFFSET - HALF_WINWIDHT
        elif heroCenterx - (camerax + HALF_WINWIDHT) > CAM_OFFSET:
            camerax = heroCenterx - CAM_OFFSET - HALF_WINWIDHT
        if (cameray + HALF_WINWIDHT) - heroCentery > CAM_OFFSET:
            cameray = heroCentery + CAM_OFFSET - HALF_WINWIDHT
        elif heroCentery - (cameray + HALF_WINWIDHT) > CAM_OFFSET:
            cameray = heroCentery - CAM_OFFSET - HALF_WINWIDHT
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()

