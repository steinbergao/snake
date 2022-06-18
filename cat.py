import pygame as pg


class Game:
	def __init__(self):
		self.map_width = 200
		self.map_height = 200
		self.window = pg.display.set_mode((self.map_width, self.map_height))
		self.cat = Cat()
		self.fps = 100
		self.speed = 99

	def draw_all(self):
		self.window.fill(pg.Color('green'))
		self.cat.draw()
		pg.display.update()

	def move_all(self):
		self.cat.move()


class Cat:
	def __init__(self):
		self.color = pg.Color((0, 100, 100))
		self.position = [100, 100]
		self.width = 20
		self.height = 20
		self.speed = 5

	def move(self):
		key = pg.key.get_pressed()
		if key[pg.K_w]:
			self.position[1] -= self.speed
		elif key[pg.K_a]:
			self.position[0] -= self.speed
		elif key[pg.K_s]:
			self.position[1] += self.speed
		elif key[pg.K_d]:
			self.position[0] += self.speed

	def draw(self):
		pg.draw.rect(game.window, self.color, (self.position[0], self.position[1], self.width, self.height))


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
			# elif event.type == pg.KEYDOWN:
			#	game.cat.move()


main()
