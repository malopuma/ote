import pygame
from pygame.key import ScancodeWrapper

from tile import Tile
import player

class Map:
    def __init__(self, image_path: str):
        self.map_array = self.load_map_from_image(image_path)
        self.offset = [232, 0]

        self.gras_tile = Tile("grass", pygame.image.load("assets/basic_gras_tile.png"))
        self.water_tile = Tile("water", pygame.image.load("assets/basic_water_tile.png"))
        self.tile_size: list = [self.gras_tile.width, self.gras_tile.height]
        self.cached_map = self.cached_map()


    # draw the map
    def draw(self, window):
        window.blit(self.cached_map, self.offset)

    # set a tile value to change the map
    def set_tile(self, row, col, value):
        if 0 <= row < len(self.input_array) and 0 <= col < len(self.input_array[0]):
            self.input_array[row][col] = value

    def load_map_from_image(self, image_path):
        # Lade das Bild
        bitmap = pygame.image.load(image_path)
        width, height = bitmap.get_size()
        
        new_map = []
        
        for y in range(height):
            row = []
            for x in range(width):
                # Hole die Farbe des Pixels an Position (x, y)
                color = bitmap.get_at((x, y))
                
                # Vergleiche RGB-Werte (ohne Alpha)
                if color[:3] == (0,0,0):
                    row.append(1)
                elif color[:3] == (1,1,1):
                    row.append(0)
                else:
                    row.append(0) # Standardwert
            new_map.append(row)
            
        return new_map
    
    def set_map_from_image(self, image_path):
        self.input_array = self.load_map_from_image(image_path)


    def set_offset(self):
        pass


    def move(self, keys: ScancodeWrapper, player: player.Player):
        if keys[pygame.K_LEFT] and player.is_touching_limit[0] == True:
            self.offset = (self.offset[0] + player.movement_interval, self.offset[1])
        if keys[pygame.K_RIGHT] and player.is_touching_limit[1] == True:
            self.offset = (self.offset[0] - player.movement_interval, self.offset[1])    
        if keys[pygame.K_UP] and player.is_touching_limit[2] == True:        
            self.offset = (self.offset[0], self.offset[1] + player.movement_interval / 2)
        if keys[pygame.K_DOWN] and player.is_touching_limit[3] == True:
            self.offset = (self.offset[0], self.offset[1] - player.movement_interval / 2)
        pass


    # Cache the map to a surface to improve performance 
    def cached_map(self) -> pygame.Surface:
        # Erstelle eine neue Oberfläche, um die Karte zu zeichnen
        chache_surface = pygame.Surface((len(self.map_array[0]) * self.gras_tile.width, len(self.map_array) * self.gras_tile.height))

        for row_index, row in enumerate(self.map_array):
            for column_index, tile in enumerate(row):
                if tile == 1:
                    chache_surface.blit(self.gras_tile.image, (chache_surface.get_width()/2 + column_index * (self.gras_tile.width / 2) - row_index * (self.gras_tile.width / 2),
                                                  row_index * (self.gras_tile.height / 2) + column_index * (self.gras_tile.height / 2)))
                elif tile == 0:
                    chache_surface.blit(self.water_tile.image, (chache_surface.get_width()/2 + column_index * (self.water_tile.width / 2) - row_index * (self.water_tile.width / 2),
                                                  row_index * (self.water_tile.height / 2) + column_index * (self.water_tile.height / 2)))
        
        return chache_surface
    
    def print_tile_size(self, keys):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_t]:
            print(f"tile size: {self.tile_size}")

