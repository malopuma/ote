# on th edges - entry point
# building game centered on calm gameplay in a stunning, evolving landscape

import pygame

#from entity import Entity
from player import Player
from game_map import Map
import positions_controller

# initialize pygame and create the window
pygame.init()
window = pygame.display.set_mode((516,516))
pygame.display.set_caption("On The Edges")
clock = pygame.time.Clock()

# create the player and the map
player = Player([0, 1024], 16, 20, 2)
map1 = Map("map2.png")
pos_controller = positions_controller.PosController(player, map1) # controller for updating the positions of the player and the map
print(f"tile size: {map1.tile_size}")

# game loop
run: bool = True
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pos_controller.update()
    player.print_positional_data(map1.tile_size)
    
    window.fill((0, 0, 0))
    map1.draw(window)
    player.draw(window)
    pygame.display.update()

    clock.tick(60)

pygame.quit()

