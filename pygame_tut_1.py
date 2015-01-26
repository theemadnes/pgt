import pygame

RESOLUTION = (800,600)
FPS = 60

pygame.init()
gameDisplay = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption('my new game')
clock = pygame.time.Clock()

crashed = False

while not crashed:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			crashed = True

		print(event)

	pygame.display.update() # could use flip, but update allows for specifying what to update
	clock.tick(FPS)

pygame.quit()
print "Exiting..."
quit()
