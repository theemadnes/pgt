import pygame

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
RESOLUTION = (DISPLAY_WIDTH,DISPLAY_HEIGHT)
FPS = 60

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

carImageLarge = pygame.image.load('images/PngMedium-Modern-Open-Top-Car-Top-View-5602.png')
carImage = pygame.transform.smoothscale(carImageLarge, (50,100))

def car(x,y):
	gameDisplay.blit(carImage, (x,y))

x = (DISPLAY_WIDTH * .4)
y = (DISPLAY_HEIGHT * .8)

pygame.init()
gameDisplay = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption('my new game')
clock = pygame.time.Clock()

crashed = False

while not crashed:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			crashed = True

		#print(event)
	gameDisplay.fill(BLACK)
	car(x,y)

	pygame.display.update() # could use flip, but update allows for specifying what to update
	clock.tick(FPS)

pygame.quit()
print "Exiting..."
quit()
