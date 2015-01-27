import pygame
import time
import random

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
RESOLUTION = (DISPLAY_WIDTH,DISPLAY_HEIGHT)
FPS = 60

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (200,0,0)
BRIGHT_RED = (255,0,0)
GREEN = (0,200,0)
BRIGHT_GREEN = (0,255,0)
BLUE = (0,0,255)


carImageLarge = pygame.image.load('images/PngMedium-Modern-Open-Top-Car-Top-View-5602.png')
carImage = pygame.transform.smoothscale(carImageLarge, (50,100))

pygame.init()
gameDisplay = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption('my new game')
clock = pygame.time.Clock()

def things_dodged(count):

	font = pygame.font.SysFont(None, 25)
	text = font.render("Dodged: " + str(count), True, RED)
	gameDisplay.blit(text, (0,0))

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

	textSurface = font.render(text, True, BLACK)

	return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, i, a):

		mouse = pygame.mouse.get_pos()
		# print mouse

		if x+w > mouse[0] > x and y+h > mouse[1] > y:

			pygame.draw.rect(gameDisplay, a, (x, y, w, h))

		else:

			pygame.draw.rect(gameDisplay, i, (x, y, w, h))

		smallText = pygame.font.Font("freesansbold.ttf", 20)
		textSurf, textRect = text_objects(msg, smallText)
		textRect.center = ((x+(w/2), y+(h/2)))
		gameDisplay.blit(textSurf, textRect)

def game_intro():

	intro = True

	while intro:

		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				pygame.quit()
				quit()

		gameDisplay.fill(WHITE)
		largeText = pygame.font.Font('freesansbold.ttf', 50)
		TextSurf, TextRect = text_objects("INTRO SCREEEEEEN", largeText)
		TextRect.center = ((DISPLAY_WIDTH/2), (DISPLAY_HEIGHT/2))
		gameDisplay.blit(TextSurf, TextRect)

		mouse = pygame.mouse.get_pos()
		# print mouse

		button("GO!", 150, 450, 100, 50, GREEN, BRIGHT_GREEN)
		button("QUIT", 550, 450, 100, 50, RED, BRIGHT_RED)

		pygame.display.update()
		clock.tick(15)

def gameLoop():

	gameExit = False

	dodged = 0

	x = (DISPLAY_WIDTH * .45)
	y = (DISPLAY_HEIGHT * .8)

	x_change = 0
	y_change = 0

	thing_start_x = random.randrange(0, DISPLAY_WIDTH)
	thing_start_y = -600
	thing_velocity = 4
	thing_width = 100
	thing_height = 60

	thingCount = 1

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
		things_dodged(dodged)

		if (x + carImage.get_width()) > DISPLAY_WIDTH or x < 0:

			crash()

		if thing_start_y > DISPLAY_HEIGHT:

			thing_start_y = 0 - thing_height
			thing_start_x = random.randrange(0, DISPLAY_WIDTH)
			dodged += 1
			# thing_velocity += 1
			thing_width += dodged * 1.2

		if y < thing_start_y + thing_height:

			if x > thing_start_x and x < thing_start_x + thing_width or x + carImage.get_width() > thing_start_x and x + carImage.get_width() < thing_start_x + thing_width:

				print ('x crossover')
				crash()

		pygame.display.update() # could use flip, but update allows for specifying what to update
		clock.tick(FPS)

game_intro()
gameLoop()

pygame.quit()
print "Exiting..."
quit()
