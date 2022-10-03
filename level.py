import pygame as pg
from player import Player, Bullet
from settings import WIDTH, HEIGHT

class Level:
    def __init__(self, display):
        self.display = display

        self.player = Player(display, WIDTH / 2, HEIGHT / 2)

        self.bullet_group = pg.sprite.Group()

        self.bullet_delay = 24

    def shooting(self, minput, mpos):
        if minput[0]:
            self.bullet_delay += 1
            if self.bullet_delay >= 10:
                Bullet(self.display, self.bullet_group, mpos, self.player.pos.copy())
                self.bullet_delay = 0

    def update(self, keys, mpos, minput):
        self.shooting(minput, mpos)
        for blt in self.bullet_group:
            blt.update()

        self.player.update(keys, mpos)