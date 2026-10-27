import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
from player import Player


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=LINE_WIDTH,
        )

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            first_split_angle = self.velocity.rotate(angle)
            second_split_angle = self.velocity.rotate(random.uniform(-20, -50))
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first_split = Asteroid(self.position.x, self.position.y, new_radius)
            first_split.velocity = first_split_angle * 1.2
            second_split = Asteroid(self.position.x, self.position.y, new_radius)
            second_split.velocity = second_split_angle * 1.2
