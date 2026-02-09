import pygame

from tile import Tile

class Map:
    def __init__(self, input_array):
        self.input_array = input_array
        self.tile_size = 32

        self.colorDIRT = (161, 199, 95)
        self.colorGRASS = (163, 168, 141)

        self.tile = Tile()


    # draw the map
    def draw(self, window):
        for row_index, row in enumerate(self.input_array):
            for column_index, tile in enumerate(row):
                if tile == 1:
                    window.blit(self.tile.image, (column_index * self.tile_size, row_index * self.tile_size))
                elif tile == 0:
                    pygame.draw.rect(window, self.colorGRASS, (column_index * self.tile_size, row_index * self.tile_size, self.tile_size, self.tile_size))

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

