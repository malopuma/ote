import pygame

class Map:
    def __init__(self, window, input_array):
        self.window = window
        self.input_array = input_array

    def draw(self, window):
        pos_x = 0
        pos_y = 64
        current_index = 0

        for y in range(4):
            pos_x = 0
            for x in range(4):
                if self.input_array[current_index] == 1:
                    pygame.draw.rect(window, (0, 0, 0), (pos_x, pos_y, 64, 64))
                else:
                    pygame.draw.rect(window, (255, 255, 255), (pos_x, pos_y, 64, 64))
                current_index += 1
                pos_x += 64
            pos_y += 64

