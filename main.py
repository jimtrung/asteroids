import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shoot import Shoot

def main():
  pygame.init()

  # Set screen
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  # Set clock fps
  clock = pygame.time.Clock()
  dt = 0

  # Create group
  updatables = pygame.sprite.Group()
  drawables = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updatables, drawables)
  Asteroid.containers = (updatables, drawables, asteroids)
  AsteroidField.containers = (updatables)
  Shoot.containers = (updatables, drawables, shots)

  # Create player object
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
  asteroid_field = AsteroidField()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    pygame.Surface.fill(screen, (0, 0, 0))
    
    for obj in updatables:
      obj.update(dt)

    for obj in drawables:
      obj.draw(screen)

    for obj in asteroids:
      if obj.collision(player):
        print("Game over!")
        sys.exit()

    for ast in asteroids:
      for sho in shots:
        if ast.collision(sho):
          ast.split()
          sho.kill()
  
    pygame.display.flip()

    passed_time = clock.tick(60)
    dt = passed_time / 1000

if __name__ == "__main__":
  main()