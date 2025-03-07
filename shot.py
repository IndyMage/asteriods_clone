import pygame
from circleshape import CircleShape
from constants import PLAYER_SHOOT_SPEED, SHOT_RADIUS, WHITE

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position.x = x
        self.position.y = y
        self.radius = SHOT_RADIUS

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

