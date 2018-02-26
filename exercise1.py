#!/usr/bin/env python
'''

For every line, please add a comment describing what it does. 

Try to describe each line within the context of the program as a whole, rather than just mechanically

Feel free to alter the parameters to see how things change. That can be a great way to be able to intuit what is supposed to be happening

I will do the first few lines for you as an example


'''
import sys, logging, pygame	# imports the sys, logging, and pygame modules so they can be used in this program
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' # requires that the Python 3.4 (or higher version) interpreter is being used; i.e., not compatible with Python 2

logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__name__)

screen_size = (800,600)
FPS = 60
red = (255,0,0)
black = (0,0,0)

class Block(pygame.sprite.Sprite):
	def __init__(self, position, direction):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((50, 50))
		self.image.fill(red)
		self.rect = self.image.get_rect()
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
	block = Block((200,200),(-1,1))
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