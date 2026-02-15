import pygame

import entity
import game_map
import player

class PosController:
    def __init__(self, player: player.Player, game_map: game_map.Map):
        self.player = player
        self.game_map = game_map


    def update(self):
        keys = pygame.key.get_pressed()
        self.update_player_pos(keys)
        self.update_player_drawing_pos_and_touching_limit(keys)
        self.update_map_pos(keys)


    def update_player_pos(self, keys):
        self.player.update_position(keys)


    def update_player_drawing_pos_and_touching_limit(self, keys):
        self.player.update_drawing_pos(keys)
        self.player.set_touching_limit(keys)


    def update_map_pos(self, keys):
        self.game_map.move(keys, self.player)
