import pygame

class Tile:
    def __init__(self, type: str, image: pygame.image):
        self.title = "Basic Grass Tile"
        self.type = type
        self.image = image
        self.width = self.image.get_width() if self.image else 0
        self.height = self.image.get_height() if self.image else 0

    def load_image(self):
        try:
            self.image = pygame.image.load(f"assets/basic_gras_tile.png")
            print(f"class Tile; {self.title}: image loaded successfully.")
            return self.image
        
        except pygame.error:
            self.image = None
            print("Error loading tile image.")
