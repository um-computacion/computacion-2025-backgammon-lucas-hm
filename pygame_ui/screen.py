import pygame, sys

class pantalla:
    size = (1920, 1080)
    pygame.init()
    screen = pygame.display.set_mode(size)

    while true:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
