import pygame
from circleshape import CircleShape
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		
		ang = random.uniform(20, 50)
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		
		asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
		asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
		asteroid1.velocity = self.velocity.rotate(ang) * 1.2
		asteroid2.velocity = self.velocity.rotate(-ang) * 1.2
		

	def draw(self, screen):
		pygame.draw.circle(
			surface=screen,
			color="white",
			center=self.position,
			radius=self.radius,
			width=2
		)

	def update(self, dt):
		self.position += self.velocity * dt