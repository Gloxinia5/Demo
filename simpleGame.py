import pygame

#initialize
pygame.init()

#Variables
WINDOW_WIDTH = 928
WINDOW_HEIGHT = 793
isRunning = True
isJump = False
jumpCount = 10

#backround
bg = pygame.image.load('Background.png')

#player
playerImg = pygame.image.load('asset/idle/Idle_01.png')
playerX = 0
playerY = 700
playerWidth = 128
playerHeight = 128
vel = 3

#Game main window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame")



#Game Loop
while isRunning:
    pygame.time.delay(20)

    playerLoop = 1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and playerX > vel:
        playerX -= vel
    if keys[pygame.K_RIGHT] and playerX < (WINDOW_WIDTH - playerWidth):
        playerX += vel
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
        if keys[pygame.K_UP] and playerY > vel:
            playerY -= vel
        if keys[pygame.K_DOWN] and playerY < (WINDOW_HEIGHT - playerHeight):
            playerY += vel
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            playerY -= jumpCount ** 2 / 2 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (playerX, playerY, playerWidth, playerHeight))
    pygame.display.update()



