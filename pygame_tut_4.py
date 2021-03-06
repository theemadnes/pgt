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

pygame.init()
gameDisplay = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption('my new game')
clock = pygame.time.Clock()



def gameLoop():

	gameExit = False

	x = (DISPLAY_WIDTH * .45)
	y = (DISPLAY_HEIGHT * .8)

	x_change = 0
	y_change = 0

	while not gameExit:

		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				gameExit = True

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_LEFT:

					x_change = -5

				elif event.key == pygame.K_RIGHT:

					x_change = 5

			if event.type == pygame.KEYUP:

				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:

					x_change = 0

			#print(event)
		x += x_change

		gameDisplay.fill(BLACK)
		car(x,y)

		if (x + carImage.get_width()) > DISPLAY_WIDTH or x < 0:

			gameExit = True

		pygame.display.update() # could use flip, but update allows for specifying what to update
		clock.tick(FPS)

gameLoop()

pygame.quit()
print "Exiting..."
quit()
