import pygame
from circleshape import CircleShape
from constants import WHITE

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        #print(f"Asteroid create at ({x}, {y}) with radius {radius}")
        super().__init__(x, y, radius)
        self.position.x = x
        self.position.y = y
        self.radius = radius
    
    def draw(self, screen):
        #print(f"Drawing asteroid at {self.position} with radius {self.radius}")
        pygame.draw.circle(screen, WHITE, (self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt