# 
import pygame
from pygame.key import ScancodeWrapper


class Entity:
    def __init__(self, pos_x: int, pos_y: int):
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.map_position: list = [0, 0]

    # moves the entity
    def move(self, keys: ScancodeWrapper):
        pass
        
    def draw(self, window):
        pass

    def get_position(self):
        return (self.pos_x, self.pos_y)
        