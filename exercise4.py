#!/usr/bin/env python
'''

For this exercise, animate random sprites using a sprite sheet


'''
import sys, logging, pygame, random, os
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' 

logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__name__)

screen_size = (800,600)
FPS = 60
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
img_size = (44,51)
img_margin = (4,4)

class Block(pygame.sprite.Sprite):
	def __init__(self, img, position, direction):
		pygame.sprite.Sprite.__init__(self)
		self.sheet = pygame.image.load(os.path.join('.', img)).convert()	# load the image from the current folder and convert it so pygame.image can use it
		(self.width,self.height) = img_size			# the width and height of the image on the sprite sheet
		(self.margin_x,self.margin_y) = img_margin	# the space between the images on the sprite sheet

		self.rect = pygame.Rect((self.margin_x,self.margin_y,self.width,self.height))
		self.image = pygame.Surface(self.rect.size).convert()
		self.image.blit(self.sheet, (0,0), self.rect)	#from the sheet, grab the correct image
		#self.image.set_colorkey(green)
		
		(self.rect.x,self.rect.y) = position
		self.direction = direction

	def update(self):
		(dx,dy) = self.direction
		self.rect.x += dx
		self.rect.y += dy
		(WIDTH,HEIGHT) = screen_size
		if self.rect.left > WIDTH:
			self.rect.right = 0
		if self.rect.right < 0:
			self.rect.left = WIDTH
		if self.rect.top > HEIGHT:
			self.rect.bottom = 0
		if self.rect.bottom < 0:
			self.rect.top = HEIGHT


def main():
	pygame.init()
	screen = pygame.display.set_mode(screen_size)
	clock = pygame.time.Clock()

	blocks = pygame.sprite.Group()
	block = Block('sprite_sheet.png',(200,200),(5,1))
	blocks.add(block)

	while True:
		clock.tick(FPS)
		screen.fill(black)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)

		blocks.update()
		blocks.draw(screen)
		pygame.display.flip()

if __name__ == '__main__':
	main()