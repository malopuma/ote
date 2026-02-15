import math

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

        self.map_position[0] = 256
        self.map_position[1] = 256
        self.width = width
        self.height = height
        self.movement_speed = movement_speed

    def move(self, keys: ScancodeWrapper):      
        if keys[pygame.K_LEFT] and self.pos_x >= 192:
            self.pos_x -= self.movement_speed

            self.map_position[0] = self.map_position[0] - int(round(math.sqrt((self.movement_speed*self.movement_speed) / 2)))
            self.map_position[1] = self.map_position[1] + int(round(math.sqrt((self.movement_speed*self.movement_speed) / 2)))
            print(f"self.map_position: {self.map_position}")

        if keys[pygame.K_RIGHT] and self.pos_x <= 320:
            self.pos_x += self.movement_speed

            self.map_position[0] = self.map_position[0] + int(round(math.sqrt((self.movement_speed*self.movement_speed) / 2)))
            self.map_position[1] = self.map_position[1] - int(round(math.sqrt((self.movement_speed*self.movement_speed) / 2)))
            print(f"self.map_position: {self.map_position}")

        if keys[pygame.K_UP] and self.pos_y >= 192:
            self.pos_y -= self.movement_speed

            self.map_position[0] = self.map_position[0] - int(round(math.sqrt((self.movement_speed*self.movement_speed) / 2)))
            self.map_position[1] = self.map_position[1] - int(round(math.sqrt((self.movement_speed*self.movement_speed) / 2)))
            print(f"self.map_position: {self.map_position}")

        if keys[pygame.K_DOWN] and self.pos_y <= 320:

            self.map_position[0] = self.map_position[0] + int(round(math.sqrt((self.movement_speed*self.movement_speed) / 2)))
            self.map_position[1] = self.map_position[1] + int(round(math.sqrt((self.movement_speed*self.movement_speed) / 2)))
            print(f"self.map_position: {self.map_position}")

            self.pos_y += self.movement_speed

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.pos_x, self.pos_y, self.width, self.height))

    def get_position(self):
        return (self.pos_x, self.pos_y)