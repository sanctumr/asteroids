from pygame.math import Vector2
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOT_SPEED, PLAYER_SHOT_COOLDOWN
import pygame # type: ignore

class Player(CircleShape):
    timer = 0

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

            # Handle timer countdown
        if self.timer > 0:  # Only subtract from the timer if it's above 0
            self.timer -= dt
        if self.timer < 0:
            self.timer = 0  # Ensure the timer doesn't go negative

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.timer <= 0:  # Only shoot if the timer is 0 or less
            velocity = Vector2(0, 1)
            velocity = velocity.rotate(self.rotation)
            velocity = velocity * PLAYER_SHOT_SPEED
            Shot(self.position.x, self.position.y, velocity)  # Fire the shot!
            self.timer = PLAYER_SHOT_COOLDOWN  # Reset the timer for cooldown