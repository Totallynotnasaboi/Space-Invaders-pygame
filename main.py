import pygame

WIDTH = 800
HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Title and Icon
pygame.display.set_caption("Space Invaders by NASA BOI")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Player
playerImg = icon = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x,y):
  screen.blit(playerImg, (x, y))

# Game Loop
running = True
while running:
  
  # RGB = Red, Green, Blue
  screen.fill((0, 0, 0))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
    # Controls
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        playerX_change = -0.1
      
      if event.key == pygame.K_RIGHT:
        playerX_change = 0.1
    
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        playerX_change = 0

  
  playerX += playerX_change
  player(playerX, playerY)
  pygame.display.update()