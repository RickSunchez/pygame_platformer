import pygame
from pygame import *

pygame.init()

screen_stat = {
	"width": 10,
	"height": 10,
	"tile": 48
}

player_stat = {
	"x": 100,
	"y": 100,
	"speed": 5,
	"jump_power": 10,
	"onGround": False,
	"dx": 0,
	"dy": 0,
	"ddy": 0.35,
	"width":  int(screen_stat["tile"]/2),
	"height": int(screen_stat["tile"]*4/5)
}

player = sprite.Sprite()
player.image = Surface((player_stat["width"], player_stat["height"]))
player.image.fill(Color("#00FF19"))

level = [
	"##########",
	"#        #",
	"#        #",
	"#        #",
	"#        #",
	"#        #",
	"#        #",
	"#        #",
	"#        #",
	"##########"
]

DISPLAY = (screen_stat["width"]*screen_stat["tile"], screen_stat["height"]*screen_stat["tile"])
screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption("Test game")

background = Surface(DISPLAY)
background.fill(Color("#ffffff"))

while 1:
	for e in pygame.event.get():
		if e.type == QUIT:
			exit()

	screen.blit(background, (0,0))

	for y in range(len(level)):
		for x in range(len(level[y])):
			coordX = x*screen_stat["tile"]
			coordY = y*screen_stat["tile"]

			if level[y][x] == "#":
				print(1)
				tile = Surface((screen_stat["tile"], screen_stat["tile"]))
				tile.fill(Color("#FF6262"))

				screen.blit(tile, (coordX, coordY))

	screen.blit(player.image, (player_stat["x"], player_stat["x"]))
	pygame.display.update()