# on th edges - entry point
# building game centered on calm gameplay in a stunning, evolving landscape

import pygame

pygame.init()

window = pygame.display.set_mode((516,516))
pygame.display.set_caption("On The Edges")

# variables
x: int = 32
y: int = 32
width: int = 16
height: int = 16
velocity: int = 10

run: bool = True

# game loop
while run == True:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()

