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

def player():
  screen.blit(playerImg, (playerX, playerY))

# Game Loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  screen.fill((0, 0, 0))
  pygame.display.update()