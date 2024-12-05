# region INTRO

import pygame
import random
import math

# Start Game
pygame.init()

# Main Screen Size
screen = pygame.display.set_mode((800, 600)) # Horizontal, Vertical

# App Title Bar
pygame.display.set_caption("Campfire Keeper")
icon = pygame.image.load('Campfire Lv3.png')
pygame.display.set_icon(icon)

# endregion

# region GENERATE UNITS ================================================================================================

# Background Image
background = pygame.image.load('BG.png')

# Player Stats
playerImg = pygame.image.load('Hero.png')
playerX = 35 # Horizontal
playerY = 450 # Vertical
playerX_move = 0
playerY_move = 0
def player(x,y):
    screen.blit(playerImg, (x,y))

# Bullet Stats
bulletImg = pygame.image.load('Bullet.png')
bulletX = 0 # Horizontal
bulletY = 0 # Vertical
bullet_speed = 8
bulletX_move = 1
bulletY_move = 0
bullet_state = "ready" # Not on screen
def bullet(x,y):
    global bullet_state
    bullet_state = "fire" # Spawn on screen
    screen.blit(bulletImg, (x + 50, y + 20)) # Where the bullet is created

def isCollision(enemyX, enemyY, bulletX, bulletY):
    vertical_scale = 1.7 # Enemy Collision Size
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow((enemyY - bulletY) * vertical_scale, 2))
    if distance < 50:
        return True
    else:
        return False

exp = 0

# Enemy Stats
enemyImg = pygame.image.load('Enemy.png')
enemyX = 850 # Horizontal
enemyY = random.randint (55,470)# Vertical
enemyX_move = 1
enemyY_move = 0
def enemy(x,y):
    screen.blit(enemyImg, (x,y))

# Summon Campfire Lv0
campfireLv0Img = pygame.image.load('Campfire Lv0.png')
# Campfire Lv0 start Location
campfireLv0X = 35 # Horizontal
campfireLv0Y = 250 # Vertical
def campfireLv0(x,y):
    screen.blit(campfireLv0Img, (x,y))

# Summon Campfire Lv1
campfireLv1Img = pygame.image.load('Campfire Lv1.png')
# Campfire Lv1 start Location
campfireLv1X = 35
campfireLv1Y = 250
def campfireLv1(x,y):
    screen.blit(campfireLv1Img, (x,y))

# Summon Campfire Lv2
campfireLv2Img = pygame.image.load('Campfire Lv2.png')
# Campfire Lv2 start Location
campfireLv2X = 35
campfireLv2Y = 250
def campfireLv2(x,y):
    screen.blit(campfireLv2Img, (x,y))

# Summon Campfire Lv3
campfireLv3Img = pygame.image.load('Campfire Lv3.png')
# Campfire Lv3 start Location
campfireLv3X = 35
campfireLv3Y = 250
def campfireLv3(x,y):
    screen.blit(campfireLv3Img, (x,y))
# endregion

# MAIN GAME LOOP =======================================================================================================
running = True
while running:

    # Insert Background image
    screen.blit(background, (0,0))

    # GAME LOOP continuation
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # KEYBIND - PRESS
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: # UP
                playerY_move = -1.5
            if event.key == pygame.K_s: # DOWN
                playerY_move = 1.5
            if event.key == pygame.K_a: # LEFT
                playerX_move = -1.5
            if event.key == pygame.K_d: # RIGHT
                playerX_move = 1.5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready": # Prevents bullet spamming
                    bulletX = playerX
                    bulletY = playerY
                    bullet_state = "fire"

        # KEYBIND - RELEASE
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w: # UP
                playerY_move = -0
            if event.key == pygame.K_s: # DOWN
                playerY_move = -0
            if event.key == pygame.K_a: # LEFT
                playerX_move = -0
            if event.key == pygame.K_d: # RIGHT
                playerX_move = -0

    # Call Player Inside Game
    player(playerX,playerY)

    # Player Movement Logic
    playerX += playerX_move
    playerY += playerY_move

    # Enemy Logic
    enemy(enemyX,enemyY)
    enemy_speed = 0.5

    # Enemy moves to the left
    if enemyX > 15:
        enemyX -= enemy_speed

    # Player Game Border
    # Horizontal border
    if playerX <=15:
        playerX = 15
    elif playerX >=730:
        playerX = 730
    # Vertical border
    if playerY <=55:
        playerY = 55
    elif playerY >=470:
        playerY = 470

    # Enemy Game Border
    # Horizontal border
    if enemyX <= 15:
        enemyX = 15
    # Vertical border
    if enemyY <= 55:
        enemyY = 55
    elif enemyY >= 470:
        enemyY = 470

    # Bullet Movement Logic
    if bullet_state == "fire":
        bullet(bulletX, bulletY)
        bulletX += bullet_speed # This determines where the bullet goes
    # Reset Bullet Once Off-Screen
    if bulletX >= 760: # Border on when this will remove the bullet from the game
        bulletX = 0 # Delete bullet from the game
        bullet_state = "ready"

    # Collision Logic
    collision = isCollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY = 0
        bullet_state = "ready"
        exp += 1
        print("exp gained: "+ str(exp))
        enemyX = 850  # Horizontal
        enemyY = random.randint(55, 470)  # Vertical

    # Call in Campfire Lv0
    campfireLv0(campfireLv0X,campfireLv0Y)

    # Refresh game screen infinitely
    pygame.display.update()
# endregion