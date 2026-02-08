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

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= velocity
    if keys[pygame.K_RIGHT]:
        x += velocity
    if keys[pygame.K_UP]:
        y -= velocity
    if keys[pygame.K_DOWN]:
        y += velocity

    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()

