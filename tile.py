import pygame

class Tile:
    def __init__(self):
        
        self.image = self.load_image()
        

    def load_image(self):
        try:
            self.image = pygame.image.load(f"assets/basic_gras_tile.png")
            print("Tile image loaded successfully.")
            return self.image
        
        except pygame.error:
            self.image = None
            print("Error loading tile image.")
