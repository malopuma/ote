# github test backwards!!

# on th edges - entry point
# building game centered on calm gameplay in a stunning, evolving landscape

import pygame
from entity import Entity
from map import Map

pygame.init()

window = pygame.display.set_mode((516,516))
pygame.display.set_caption("On The Edges")

# variables
pos_x: int = 256
pos_y: int = 256
width: int = 16
height: int = 16
velocity: int = 10

player = Entity(256, 256, 16, 16, 10)
map1 = Map([[1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1]])

run: bool = True

# game loop
while run == True:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player.move()
    
    window.fill((0, 0, 0))
    map1.draw(window)
    player.draw(window)
    pygame.display.update()

pygame.quit()

