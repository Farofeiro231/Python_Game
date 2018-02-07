import pygame, sys
from pygame.locals import *


pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

fontObj = pygame.font.Font('freesansbold.ttf', 32) #Font object created
'''
The parameters are the text, a boolean indicating the presence of anti-aliasing, the font color and background color
'''
textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE) #Surface with text created
'''
#Creates a rectangle from the writen surface with the right size to contain the text and top left corner at (0,0)
'''
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150) #Changes the center of the retangle to the given coordinates

while True:# main game loop
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj) #Copy the writen surface rectangle into the initial surface
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()