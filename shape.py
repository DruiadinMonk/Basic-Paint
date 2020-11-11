# Class to draw shape on mouse (x, y).

# MODULES
import pygame
from colors import Colors



# SHAPE CLASS
class Shape:


	# INITIALIZE: Generic shape needs as MUCH inputs initially as possible. Circle, square, and triangle.
	def __init__(self, shape, window, color, x1, y1, x2, y2, x3, y3, w, h, radius, tx1, ty1, tx2, ty2, tx3, ty3):
		self.shape = shape 		# 	0 = Circle, 1 = Square, 2 = Triangle
		self.window = window
		self.color = color
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.x3 = x3
		self.y3 = y3
		self.w = w
		self.h = h
		self.radius = radius
		self.tx1 = tx1
		self.ty1 = ty1
		self.tx2 = tx2
		self.ty2 = ty2
		self.tx3 = tx3
		self.ty3 = ty3


	# DRAW: 'Shape' = initial shape. Change in 'Main Loop'.
	def draw(self):

		# CIRCLE
		if self.shape == "Circle":
			pygame.draw.circle(self.window, self.color, (self.x1, self.y1), self.radius)

		# SQUARE
		if self.shape == "Square":
			pygame.draw.rect(self.window, self.color, (self.x1, self.y1, self.w, self.h))

		# TRIANGLE (X, Y): tx1, ty1, tx2, ty2, tx3, ty3
		if self.shape == "Triangle": 	# Point Order: Bottom Left, TOP, Bottom Right
			pygame.draw.polygon(self.window, self.color, [(self.x1-self.tx1, self.y1+self.ty1), (self.x2, self.y2-self.ty2), (self.x3+self.tx3, self.y3+self.ty3)])



		# BUTTON 6: Triangle [(x1, y1), (x2, y2), (x3, y3)]
		# if number == 5: 	pygame.draw.polygon(self.window, self.color, [(self.x + 20, self.y + 5), (self.x + 35, self.y + 35), (self.x + 5, self.y + 35)])
