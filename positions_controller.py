import pygame

import entity
import game_map
import player

class PosController:
    def __init__(self, player: player.Player, game_map: game_map.Map):
        self.player = player
        self.game_map = game_map
        pass

    def update(self):
        keys = pygame.key.get_pressed()
        self.update_player_pos(keys)
        self.update_map_pos(keys)
        pass

    def update_player_pos(self, keys):
        self.player.move(keys)
        pass

    def update_map_pos(self, keys):
        self.game_map.move(keys, self.player)
        pass