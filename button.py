# Button class to create button objects in Paint.

# MODULES
import pygame
from colors import Colors



# BUTTON CLASS
class Button:

	# INTIIALIZE
	def __init__(self, window, color, x, y, w, h):
		self.window = window
		self.color = color
		self.x = x
		self.y = y
		self.w = w
		self.h = h


	# DRAW BUTTON & IMAGE: Draw square button and image over it, depending on 'number' value.
	def draw(self, number):

		pygame.draw.rect(self.window, self.color, (self.x, self.y, self.w, self.h), 1)

		# BUTTON 1: Small 'S'
		if number == 0: 	pygame.draw.circle(self.window, self.color, (self.x + 20, self.y + 20), 5)
		# BUTTON 2: Medium 'M'
		if number == 1: 	pygame.draw.circle(self.window, self.color, (self.x + 20, self.y + 20), 10)
		# BUTTON 3: Large 'L'
		if number == 2: 	pygame.draw.circle(self.window, self.color, (self.x + 20, self.y + 20), 15)
		# BUTTON 4: Circle
		if number == 3: 	pygame.draw.circle(self.window, self.color, (self.x + 20, self.y + 20), 15)
		# BUTTON 5: Square
		if number == 4: 	pygame.draw.rect(self.window, self.color, (self.x + 5, self.y + 5, 30, 30))
		# BUTTON 6: Triangle [(x1, y1), (x2, y2), (x3, y3)]
		if number == 5: 	pygame.draw.polygon(self.window, self.color, [(self.x + 20, self.y + 5), (self.x + 35, self.y + 35), (self.x + 5, self.y + 35)])
		# BUTTON 7: White
		if number == 6: 	pygame.draw.rect(self.window, Colors["WHITE"], (self.x + 1, self.y + 1, 38, 38))
		# BUTTON 8: Gray
		if number == 7: 	pygame.draw.rect(self.window, Colors["GRAY"], (self.x + 1, self.y + 1, 38, 38))
		# BUTTON 9: Black
		if number == 8: 	pygame.draw.rect(self.window, Colors["BLACK"], (self.x + 1, self.y + 1, 38, 38))
		# BUTTON 10: Red
		if number == 9: 	pygame.draw.rect(self.window, Colors["RED"], (self.x + 1, self.y + 1, 38, 38))
		# BUTTON 11: Orange
		if number == 10: 	pygame.draw.rect(self.window, Colors["ORANGE"], (self.x + 1, self.y + 1, 38, 38))
		# BUTTON 12: Yellow
		if number == 11: 	pygame.draw.rect(self.window, Colors["YELLOW"], (self.x + 1, self.y + 1, 38, 38))
		# BUTTON 13: Green
		if number == 12: 	pygame.draw.rect(self.window, Colors["GREEN"], (self.x + 1, self.y + 1, 38, 38))
		# BUTTON 14: BLue
		if number == 13: 	pygame.draw.rect(self.window, Colors["BLUE"], (self.x + 1, self.y + 1, 38, 38))
		# BUTTON 15: Purple
		if number == 14: 	pygame.draw.rect(self.window, Colors["PURPLE"], (self.x + 1, self.y + 1, 38, 38))
		# BUTTON 16: Big 'X', Erase ALL.
		if number == 15: 	
			pygame.draw.line(self.window, Colors["RED"], (self.x + 3, self.y +  3), (self.x + 37, self.y + 37), 3)
			pygame.draw.line(self.window, Colors["RED"], (self.x + 3, self.y + 37), (self.x + 37, self.y +  3), 3)
