import pygame

#initialize
pygame.init()

#Variables
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
isRunning = True

#Game main window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame")

#Game Loop
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    window.fill((255, 0, 0))
    pygame.display.update()

