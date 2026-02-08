import pygame

class Map:
    def __init__(self, input_array):
        self.input_array = input_array
        self.tile_size = 64

        self.colorDIRT = {161, 199, 95}
        self.colorGRASS = {163, 168, 141}

    # draw the map
    def draw(self, window):
        for row_index, row in enumerate(self.input_array):
            for column_index, tile in enumerate(row):
                if tile == 1:
                    pygame.draw.rect(window, self.colorDIRT, (column_index * self.tile_size, row_index * self.tile_size, self.tile_size, self.tile_size))
                elif tile == 0:
                    pygame.draw.rect(window, self.colorGRASS, (column_index * self.tile_size, row_index * self.tile_size, self.tile_size, self.tile_size))

