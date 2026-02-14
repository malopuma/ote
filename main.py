# on th edges - entry point
# building game centered on calm gameplay in a stunning, evolving landscape

import pygame

#from entity import Entity
from player import Player
from game_map import Map
import positions_controller

pygame.init()

window = pygame.display.set_mode((516,516))
pygame.display.set_caption("On The Edges")

# variables
pos_x: int = 256
pos_y: int = 256
width: int = 16
height: int = 16
velocity: int = 10

clock = pygame.time.Clock()

player = Player(256, 256, 8, 12, 10)
map1 = Map([[1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1]])

map1.set_map_from_image("map2.png")

# The position controller updates the positions of all the parts
# of the game
pos_controller = positions_controller.PosController(player, map1)

run: bool = True

# game loop
while run == True:
    #pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pos_controller.update()
    
    window.fill((0, 0, 0))
    map1.draw(window)
    player.draw(window)
    pygame.display.update()

    clock.tick(60)

pygame.quit()

