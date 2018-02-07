import pygame, time

pygame.init()
soundObj = pygame.mixer.Sound('beep-01a.wav')
soundObj.play()

pygame.mixer.music.load('noo.mp3') #plays the backgournd sound
pygame.mixer.music.play(-1, 0.0) #plays it forever (-1) and from the beginning (0.0)

time.sleep(10)

soundObj.stop()
pygame.mixer.music.stop()
