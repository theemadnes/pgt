import pygame
import time
import random

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
RESOLUTION = (DISPLAY_WIDTH,DISPLAY_HEIGHT)
FPS = 60

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

carImageLarge = pygame.image.load('images/car_square.png')
carImage = pygame.transform.smoothscale(carImageLarge, (50,100))

pygame.init()
gameDisplay = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption('my new game')
clock = pygame.time.Clock()
'''
def things(thing_x, thing_y, thing_w, thing_h, color):

	pygame.draw.rect(gameDisplay, color, [thing_x, thing_y, thing_w, thing_h])

def car(x,y):
	
	gameDisplay.blit(carImage, (x,y))

def crash():

	message_display('You crashed....')

def message_display(text):

	largeText = pygame.font.Font('freesansbold.ttf', 50)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((DISPLAY_WIDTH/2), (DISPLAY_HEIGHT/2))
	gameDisplay.blit(TextSurf, TextRect)


	pygame.display.update()
	time.sleep(2)

	gameLoop()

def text_objects(text, font):

	textSurface = font.render(text, True, RED)

	return textSurface, textSurface.get_rect()

def gameLoop():

	gameExit = False

	x = (DISPLAY_WIDTH * .45)
	y = (DISPLAY_HEIGHT * .8)

	x_change = 0
	y_change = 0

	thing_start_x = random.randrange(0, DISPLAY_WIDTH)
	thing_start_y = -600
	thing_velocity = 7
	thing_width = 100
	thing_height = 60

	while not gameExit:

		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				pygame.quit()
				quit()

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
		things(thing_start_x, thing_start_y, thing_width, thing_height, WHITE)
		thing_start_y += thing_velocity


		car(x,y)

		if (x + carImage.get_width()) > DISPLAY_WIDTH or x < 0:

			crash()

		if thing_start_y > DISPLAY_HEIGHT:

			thing_start_y = 0 - thing_height
			thing_start_x = random.randrange(0, DISPLAY_WIDTH)

		if y < thing_start_y + thing_height:

			if x > thing_start_x and x < thing_start_x + thing_width or x + carImage.get_width() > thing_start_x and x + carImage.get_width() < thing_start_x + thing_width:

				print ('x crossover')
				crash()

		pygame.display.update() # could use flip, but update allows for specifying what to update
		clock.tick(FPS)

gameLoop()
'''

def draw_image():

	pygame.draw.rect(gameDisplay, RED, (DISPLAY_WIDTH/2,DISPLAY_HEIGHT/2,20,20), 100)
	pygame.display.update()

'''def rot_center(image, angle):
        """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image'''

def rot_center(image, angle):
    """rotate a Surface, maintaining position."""

    loc = image.get_rect().center
    rot_sprite = pygame.transform.rotate(image, angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite

def square_loop(carImage):

	gameExit = False
	x = (DISPLAY_WIDTH / 2)
	y = (DISPLAY_HEIGHT / 2)
	rotation = 0

	while not gameExit:

		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_LEFT:

					rotation = -1

				elif event.key == pygame.K_RIGHT:

					rotation = 1

			if event.type == pygame.KEYUP:

				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:

					rotation = 0

			#print(event)
		# x += x_change

		carImage = rot_center(carImage, rotation)
		gameDisplay.blit(carImage, (x,y))
		pygame.display.update()
		gameDisplay.fill(BLACK)
	


square_loop(carImage)
pygame.quit()
print "Exiting..."
quit()
