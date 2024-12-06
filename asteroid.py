from circleshape import CircleShape
import pygame
import constants
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        velocities = [self.velocity.rotate(-angle), self.velocity.rotate(angle)]
        for velocity in velocities:
            new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid.velocity = velocity * 1.2
