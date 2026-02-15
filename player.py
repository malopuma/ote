import math

import pygame


from pygame.key import ScancodeWrapper

from entity import Entity


class Player(Entity):
    def __init__(
        self,
        position: list,
        width: int,
        height: int,
        movement_speed: int):

        # Inherit from Entity
        super().__init__(position)

        # The position on the display window, where the player is actually drawn.
        self.drawing_pos: list = [256, 256]

        self.width = width
        self.height = height
        self.movement_speed = movement_speed

        # Convert movement speed to movement interval for diagonal movement
        self.movement_interval = int(round(math.sqrt((self.movement_speed*self.movement_speed) / 2)))


    def update_position(self, keys: ScancodeWrapper):      
        if keys[pygame.K_LEFT]:
            self.position[0], self.position[1] = self.position[0] - self.movement_interval, self.position[1] + self.movement_interval
            
        if keys[pygame.K_RIGHT]:
            self.position[0], self.position[1] = self.position[0] + self.movement_interval, self.position[1] - self.movement_interval

        if keys[pygame.K_UP]:
            self.position[0], self.position[1] = self.position[0] - self.movement_interval, self.position[1] - self.movement_interval

        if keys[pygame.K_DOWN]:
            self.position[0], self.position[1] = self.position[0] + self.movement_interval, self.position[1] + self.movement_interval

        print(f"self.position: {self.position}")


    def update_drawing_pos(self, keys: ScancodeWrapper):
        if keys[pygame.K_LEFT] and self.drawing_pos[0] >= 192:
            self.drawing_pos[0] -= self.movement_interval

        if keys[pygame.K_RIGHT] and self.drawing_pos[0] <= 320:
            self.drawing_pos[0] += self.movement_interval
    
        if keys[pygame.K_UP] and self.drawing_pos[1] >= 192:
            self.drawing_pos[1] -= self.movement_interval / 2
            
        if keys[pygame.K_DOWN] and self.drawing_pos[1] <= 320:
            self.drawing_pos[1] += self.movement_interval / 2

        print(f"self.drawing_pos: {self.drawing_pos}")


    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.drawing_pos[0], self.drawing_pos[1], self.width, self.height))


    def get_position(self):
        return (self.position)