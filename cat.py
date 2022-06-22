import pygame as pg
import random
import math


class Game:
	def __init__(self):
		self.F_S = 50
		self.map_width = 800
		self.map_height = 600
		self.window = pg.display.set_mode((self.map_width, self.map_height + self.F_S))
		self.cats = []
		self.mice = []

		self.font = pg.font.Font(None, 20)
		self.fps = 100
		self.speed = 99

	def init(self):
		for i in range(0, 3):
			mouse = Mouse()
			self.mice.append(mouse)
		cat = Cat(pg.K_a, pg.K_d, pg.K_w, pg.K_s)
		self.cats.append(cat)
		cat = Cat(pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN)
		self.cats.append(cat)

	def move_all(self):
		for cat in self.cats:
			cat.move()
		for mouse in self.mice:
			mouse.move()
		for cat in self.cats:
			cat.collide()

	def draw_all(self):
		self.window.fill(pg.Color('green'))
		for cat in self.cats:
			cat.draw()
		for mouse in self.mice:
			mouse.draw()

		pg.draw.rect(self.window, "gray", (0, self.map_height, self.map_width, self.map_height + self.F_S))

		text = self.font.render("Cat1: " + str(self.cats[0].score), 1, (0, 0, 255))
		self.window.blit(text, (20, self.map_height + self.F_S // 2))

		text = self.font.render("Cat2: " + str(self.cats[1].score), 1, (255, 0, 0))
		self.window.blit(text, (self.map_width // 4 + self.map_width // 2, self.map_height + self.F_S // 2))

		pg.display.update()


class Mouse:
	def __init__(self):
		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)
		self.color = pg.Color((r, g, b))
		x = random.randint(int(game.map_width*0.1), int(game.map_width*0.9))
		y = random.randint(int(game.map_height*0.1), int(game.map_height*0.9))
		self.position = [x, y]
		self.radius = 10
		self.speed = 5

	def move(self):
		dx = random.randint(-self.speed, self.speed)
		while self.position[0] - self.radius + dx < 0 or self.position[0] + self.radius + dx > game.map_width:
			dx = random.randint(-self.speed, self.speed)

		dy = random.randint(-self.speed, self.speed)
		while self.position[1] - self.radius + dy < 0 or self.position[1] + self.radius + dy > game.map_height-game.F_S:
			dy = random.randint(-self.speed, self.speed)

		self.position[0] = self.position[0] + dx
		self.position[1] = self.position[1] + dy

	def appear(self):
		x = random.randint(int(game.map_width*0.1), int(game.map_width*0.9))
		y = random.randint(int(game.map_height*0.1), int(game.map_height*0.9))
		self.position = [x, y]

	def draw(self):
		pg.draw.circle(game.window, self.color, (self.position[0], self.position[1]), self.radius)


class Cat:
	def __init__(self, left, right, up, down):
		self.color = pg.Color((0, 100, 100))
		self.position = [random.randint(100, 600), random.randint(100, 400)]
		self.radius = 20
		self.speed = 2
		self.score = 0
		self.k_left = left
		self.k_right = right
		self.k_up = up
		self.k_down = down

	def move(self):
		key = pg.key.get_pressed()
		if key[self.k_up]:
			if self.position[1] - self.radius - self.speed > 0:
				self.position[1] -= self.speed
			else:
				self.position[1] = self.radius
		elif key[self.k_left]:
			if self.position[0] - self.radius - self.speed > 0:
				self.position[0] -= self.speed
			else:
				self.position[0] = self.radius
		elif key[self.k_down]:
			if self.position[1] + self.radius + self.speed < game.map_height-game.F_S:
				self.position[1] += self.speed
			else:
				self.position[1] = game.map_height - self.radius - game.F_S
		elif key[self.k_right]:
			if self.position[0] + self.radius + self.speed < game.map_width:
				self.position[0] += self.speed
			else:
				self.position[0] = game.map_width - self.radius

	def collide(self):
		for mouse in game.mice:
			if math.sqrt(math.pow(self.position[0] - mouse.position[0], 2) +
						math.pow(self.position[1] - mouse.position[1], 2)) < self.radius + mouse.radius:
				mouse.appear()
				self.score += 1

	def draw(self):
		pg.draw.circle(game.window, self.color, (self.position[0], self.position[1]), self.radius)


pg.init()
game = Game()
game.init()


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
