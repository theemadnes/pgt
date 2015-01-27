import pygame

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
RESOLUTION = (DISPLAY_WIDTH,DISPLAY_HEIGHT)
FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

gameDisplay = pygame.display.set_mode(RESOLUTION)
gameDisplay.fill(BLACK)

pixAr = pygame.PixelArray(gameDisplay) # could be any surface object 
pixAr[10][20] = GREEN

pygame.draw.line(gameDisplay, BLUE, (100,200), (300, 450), 5)

pygame.draw.rect(gameDisplay, RED, (400, 400, 50, 25))

pygame.draw.circle(gameDisplay, WHITE, (150,150), 75)

pygame.draw.polygon(gameDisplay, GREEN, ((25,75),(75,125),(250,375),(400,25)))

while True:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			pygame.quit()
			quit()

	pygame.display.update()

