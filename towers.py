import pygame

class Tower:
    def __init__(self, game):
        self.max_hp = 0
        self.hp = self.max_hp
        self.range = 0
        self.sell_value = 0
        self.game = game

    def sell(self):
        self.game.money += self.sell_value
        del self