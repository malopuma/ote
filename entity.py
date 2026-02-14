# 
import pygame


class Entity:
    def __init__(self, pos_x: int, pos_y: int):
        self.pos_x = pos_x
        self.pos_y = pos_y

    # moves the entity
    def move(self):
        pass
        
    def draw(self, window):
        pass

    def get_position(self):
        return (self.pos_x, self.pos_y)
        