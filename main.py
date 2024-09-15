# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
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

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	asteroid_field = AsteroidField()

	Player.containers = (updatable, drawable)
	player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

	Shot.containers = (shots, updatable, drawable)

	dt = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		for obj in updatable:
			obj.update(dt)

		for asteroid in asteroids:
			if asteroid.collides_with(player) == True:
				print("Game over!")
				sys.exit()

		for asteroid in asteroids:
			for shot in shots:
				if asteroid.collides_with(shot) == True:
					asteroid.split()
					shot.kill()

		screen.fill(color="black")

		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()

		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()