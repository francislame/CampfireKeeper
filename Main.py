import pygame

# This will initiate the game.
pygame.init()

# This will create the main screen. ((x - horizontal,y - vertical))
screen = pygame.display.set_mode((800, 600))

# Title and Icon on App Title Bar
pygame.display.set_caption("Campfire Keeper")
icon = pygame.image.load('Campfire Keeper Icon 32x.png')
pygame.display.set_icon(icon)

# Player Data
playerImg = pygame.image.load('Hero.png')
# Player start location.
playerX = 370 # Vertical
playerY = 480 # Horizontal

def player():
    screen.blit(playerImg, (playerX, playerY))

# GAME LOOP: To prevent the "not responding" error.
# Always put everything for the game inside the 'for' GAME LOOP.
running = True
while running:

    # Insert Screen Background Color (RGB)
    screen.fill((13, 30, 81))

    # GAME LOOP continuation
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Put player inside game.
    player()

    # Update game screen
    pygame.display.update()