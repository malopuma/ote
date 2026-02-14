import pygame
from pygame.key import ScancodeWrapper

from entity import Entity


class Player(Entity):
    def __init__(
        self,
        pos_x: int,
        pos_y: int,
        width: int,
        height: int,
        movement_speed: int):

        super().__init__(pos_x, pos_y)
        
        self.width = width
        self.height = height
        self.movement_speed = movement_speed

    def move(self, keys: ScancodeWrapper):      
        if keys[pygame.K_LEFT] and self.pos_x >= 192:
            self.pos_x -= self.movement_speed
            print(f"self.pos_x: {self.pos_x}")
        if keys[pygame.K_RIGHT] and self.pos_x <= 320:
            self.pos_x += self.movement_speed
        if keys[pygame.K_UP] and self.pos_y >= 192:
            self.pos_y -= self.movement_speed
        if keys[pygame.K_DOWN] and self.pos_y <= 320:
            self.pos_y += self.movement_speed

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.pos_x, self.pos_y, self.width, self.height))

    def get_position(self):
        return (self.pos_x, self.pos_y)