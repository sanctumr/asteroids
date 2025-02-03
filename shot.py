from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame # type:ignore

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius,2)
    
    def update(self, dt):
        self.position += self.velocity * dt