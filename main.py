# github test!!

# on th edges - entry point
# building game centered on calm gameplay in a stunning, evolving landscape

import pygame

pygame.init()

window = pygame.display.set_mode((516,516))
pygame.display.set_caption("On The Edges")

# variables
x: int = 256
y: int = 256
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

    if keys[pygame.K_LEFT] and x > 192:
        x -= velocity
    if keys[pygame.K_RIGHT] and x < 320:
        x += velocity
    if keys[pygame.K_UP] and y > 192:
        y -= velocity
    if keys[pygame.K_DOWN] and y < 320:
        y += velocity

    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()

