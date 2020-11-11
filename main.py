# Simple Paint program

# MODULES
import pygame
import sys
from button import Button
from colors import Colors
from shape import Shape


# INITIALIZE
pygame.init()
WIN_X, WIN_Y = 640, 600
window = pygame.display.set_mode((WIN_X, WIN_Y))
pygame.display.set_caption('Paint')
clock = pygame.time.Clock()
run = True
FPS = 60
window.fill(Colors["BLACK"]) 	 			# initial background = BLACK
MOUSE_X, MOUSE_Y 	= pygame.mouse.get_pos()



# INITIALIZE OBJECTS

# BUTTONS
button = [] 	# 6 Colors, 3 shapes, 3 sizes of brushes.
x = y = 0 		# Starting point of 1st button.
w = h = 25 		# Size of button.

for i in range(15): 	# 15 buttons
	b = Button(window, Colors["L_GRAY"], x, y, 40, 40)
	button.append(b)

	y += 40 			# Next button = down.

# After menu on left side is full, add a CLEAR button on top right corner.
b = Button(window, Colors["L_GRAY"], 600, 560, 40, 40)
button.append(b)


# SHAPE: Modify factors during 'main loop'.
# OBJECT(self, shape, window, color, x1, y1, x2, y2, x3, y3, w, h, radius, tx1, ty1, tx2, ty2, tx3, ty3):
shape = Shape("Circle", window, Colors["GRAY"], MOUSE_X, MOUSE_Y, MOUSE_X, MOUSE_Y, MOUSE_X, MOUSE_Y, 40, 40, 15, 15, 15, 15, 15, 15, 15)



# MAIN LOOP
while run:


	# INITIALIZE
	clock.tick(FPS) 							# Speed of game
	MOUSE_X, MOUSE_Y = pygame.mouse.get_pos() 	# Update mouse (x, y)
	shape.x1, shape.y1 = MOUSE_X, MOUSE_Y 		# Update object (x, y)
	shape.x2, shape.y2 = MOUSE_X, MOUSE_Y 		# Update object (x, y)
	shape.x3, shape.y3 = MOUSE_X, MOUSE_Y 		# Update object (x, y)


	# EACH EVENT
	for event in pygame.event.get():

		# IF QUIT...
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()


		# Event ONCE, then moves on. (Other than 'if pygame.mouse.get_pressed()[0]:')
		if event.type == pygame.MOUSEBUTTONDOWN:

			# CHECK ALL BUTTONS
			for i in range(len(button)):

				# BUTTON CHECK: If mouse (x, y) is in between the button borders...
				if button[i].x <= MOUSE_X <= button[i].x + 40 and button[i].y <= MOUSE_Y <= button[i].y + 40:
				
					# SIZE: Update ALL shape's sizes. (Circle, Square, Triangle)
					# BUTTON 1: Small 'S'
					if i == 0: 	
						shape.radius = 5 	
						shape.w = shape.h = 10
						shape.tx1 = shape.ty1 = 5 	# Point 1
						shape.tx2 = shape.ty2 = 5 	# Point 2
						shape.tx3 = shape.ty3 = 5 	# Point 3

					# BUTTON 2: Medium 'M'
					if i == 1:
						shape.radius = 10	
						shape.w = shape.h = 20
						shape.tx1 = shape.ty1 = 10 	# Point 1
						shape.tx2 = shape.ty2 = 10	# Point 2
						shape.tx3 = shape.ty3 = 10	# Point 3

					# BUTTON 3: Large 'L'
					if i == 2:
						shape.radius = 15	
						shape.w = shape.h = 30
						shape.tx1 = shape.ty1 = 15 	# Point 1
						shape.tx2 = shape.ty2 = 15 	# Point 2
						shape.tx3 = shape.ty3 = 15 	# Point 3

					# SHAPE: Circle, Square, and Triangle are UNIQUE functions.
					if i == 3: 		shape.shape = "Circle" 	# BUTTON 3: Large 'L'
					if i == 4: 		shape.shape = "Square" 	# BUTTON 3: Large 'L'
					if i == 5: 		shape.shape = "Triangle" 	# BUTTON 3: Large 'L'

					# COLORS
					if i == 6: 		shape.color = Colors["WHITE"] 	# BUTTON 7: White
					if i == 7: 		shape.color = Colors["GRAY"] 	# BUTTON 8: White
					if i == 8: 		shape.color = Colors["BLACK"] 	# BUTTON 9: White
					if i == 9: 		shape.color = Colors["RED"] 	# BUTTON 10: White
					if i == 10: 	shape.color = Colors["ORANGE"] 	# BUTTON 11: White
					if i == 11: 	shape.color = Colors["YELLOW"] 	# BUTTON 12: White
					if i == 12: 	shape.color = Colors["GREEN"] 	# BUTTON 12: White
					if i == 13: 	shape.color = Colors["BLUE"] 	# BUTTON 12: White
					if i == 14: 	shape.color = Colors["PURPLE"] 	# BUTTON 12: White

					# CLEAR SCREEN
					if i == 15: 	window.fill(Colors["BLACK"])

		# CONTINUOUS EVENT. (Other than 'if event.type == pygame.MOUSEBUTTONDOWN:')
		if pygame.mouse.get_pressed()[0]:

			# Draw shape
			shape.draw()


	# DRAW OBJECTS: 'i' is synced up with ALL button images, as all have a unique image to display.
	for i in range(len(button)):
		button[i].draw(i)


	# UPDATE
	pygame.display.update()
