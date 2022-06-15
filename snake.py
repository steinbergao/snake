import pygame as pg
import random


class Game:
	def __init__(self):
		self.cell_size = 50
		self.map_width = 10
		self.map_height = 10
		self.window = pg.display.set_mode([self.map_width*self.cell_size, self.map_height*self.cell_size])
		self.snake = Snake(pg.Color('blue'))
		self.apple = Apple()
		self.rack = Rack()
		self.fps = 100
		self.speed = 50

	def move_all(self):
		self.snake.move()
		self.apple.move()
		self.rack.move()

	def draw_all(self):
		self.window.fill(pg.Color('green'))
		self.snake.draw()
		self.apple.draw()
		self.rack.draw()
		pg.display.update()

	def restart(self):
		self.snake.body = [[1, 1]]


class Rack:
	def __init__(self):
		self.color = pg.Color((0, 200, 100))
		self.position = [6, 8]
		self.dx = 0
		self.dy = 1
		self.size = 50

	def draw(self):
		pg.draw.rect(game.window, self.color, (self.position[0]*game.cell_size, self.position[1]*game.cell_size,
																			self.size, self.size))

	def move(self):
		if self.position[1] > game.map_height - 2 or self.position[1] < 1:
			self.dy *= -1
		self.position[1] += self.dy

	def replace(self):
		self.position = [random.randint(0, game.map_width-1), random.randint(0, game.map_height-1)]


class Apple:
	def __init__(self):
		self.color = pg.Color('red')
		self.position = [4, 3]
		self.dx = 1
		self.dy = 0
		self.size = 50  # game.cell_size

	def draw(self):
		pg.draw.rect(game.window, self.color, (self.position[0]*game.cell_size, self.position[1]*game.cell_size,
																			self.size, self.size))

	def move(self):
		if game.map_width-2 < self.position[0] or self.position[0] < 1:
			self.dx *= -1
		# dx = random.randint(-1, 1)
		x = self.position[0] + self.dx
		# if dx == 0:
		#	dy = random.randint(-1, 1)
		# else:
		#	dy = 0

		y = self.position[1] + self.dy

		self.position = [x, y]

	def replace(self):
		self.position = [random.randint(0, game.map_width-1), random.randint(0, game.map_height-1)]


class Snake:
	def __init__(self, color):
		self.color = color
		self.body = [[1, 1]]
		self.direction = 1, 0
		self.size = 50  # game.cell_size

	def move(self):
		self.body[0][0] += self.direction[0]
		self.body[0][1] += self.direction[1]

		if self.is_apple():
			game.apple.replace()

		if self.is_rack():
			game.rack.replace()

		if self.is_wall():
			game.restart()

	def is_rack(self):
		return game.rack.position == self.body[0]

	def is_apple(self):
		return game.apple.position == self.body[0]

	def is_wall(self):
		return self.body[0][0] < 0 or self.body[0][0] > game.map_width-1 or\
				self.body[0][1] < 0 or self.body[0][1] > game.map_height-1

	def change_direction(self):
		key = pg.key.get_pressed()
		if key[pg.K_w]:
			self.direction = 0, -1
		if key[pg.K_s]:
			self.direction = 0, 1
		if key[pg.K_a]:
			self.direction = -1, 0
		if key[pg.K_d]:
			self.direction = 1, 0

	def draw(self):
		for block in self.body:
			pg.draw.rect(game.window, self.color, (block[0]*game.cell_size, block[1]*game.cell_size, self.size,
												self.size))


pg.init()
game = Game()


def main():
	clock = pg.time.Clock()
	count = 0
	while 1 > 0:
		clock.tick(game.fps)
		count += 1

		if count % (game.fps - game.speed) == 0:
			game.move_all()
			game.draw_all()

		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				exit()
			elif event.type == pg.KEYDOWN:
				game.snake.change_direction()


main()
