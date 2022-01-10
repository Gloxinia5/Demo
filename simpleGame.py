import pygame

#initialize
pygame.init()

#Variables
WINDOW_WIDTH = 928
WINDOW_HEIGHT = 793
isRunning = True

#backround
bg = pygame.image.load('asset/Backround.png')

#player
#Game main window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame")

#Game Loop
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    window.fill((69, 69, 69))
    pygame.display.update()


