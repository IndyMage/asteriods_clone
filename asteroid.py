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

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            #print("Printing the IF")
            return
        else:
            random_angle = random.uniform(20, 50)
            new_velocity1 = self.velocity.rotate(random_angle)
            new_velocity2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            #print("We are about to spawn!")
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            
            new_asteroid1.velocity = new_velocity1 * 1.2
            new_asteroid2.velocity = new_velocity2 * 1.2

            for group in self.groups():
                group.add(new_asteroid1)
                group.add(new_asteroid2)