# 
from pygame.key import ScancodeWrapper

class Entity:
    def __init__(self, position: list):
        self.position = position

    # moves the entity
    def update_position(self, keys: ScancodeWrapper):
        pass
        
    def draw(self, window):
        pass

    def set_position(self, position: list):
        self.position = position

    def get_position(self) -> list:
        return self.position
        