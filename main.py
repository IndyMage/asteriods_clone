# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots_group, updatable, drawable)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2), shots_group)
    asteroid_field = AsteroidField()

    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        screen.fill((BLACK))
        updatable.update(dt)
        shots_group.update(dt)
        
        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                print("Game over!")
                exit()
        for each in drawable:
            #print(f"Drawing {each} at {each.position} with radius {each.radius}")
            each.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()