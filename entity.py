# 
import pygame


class Entity:
    def __init__(self, pos_x: int, pos_y: int, width: int, height: int, movement_speed: int):

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.movement_speed = movement_speed

    # moves the entity
    def move(self):
        keys = pygame.key.get_pressed()        
        if keys[pygame.K_LEFT] and self.pos_x > 192:
            self.pos_x -= self.movement_speed
        if keys[pygame.K_RIGHT] and self.pos_x < 320:
            self.pos_x += self.movement_speed
        if keys[pygame.K_UP] and self.pos_y > 192:
            self.pos_y -= self.movement_speed
        if keys[pygame.K_DOWN] and self.pos_y < 320:
            self.pos_y += self.movement_speed
        
    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.pos_x, self.pos_y, self.width, self.height))
        