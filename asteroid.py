import pygame
import random
from circleshape import CircleShape
from constants import WHITE, ASTEROID_MIN_RADIUS

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

    def split(self)
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            positive_angle = pygame.Vector2(random_angle)
            negative_angle = pygame.Vector2(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            
            
            
            pygame.draw.circle(screen, WHITE, (self.position.x, self.position.y), self.radius, 2)