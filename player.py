import pygame as pg
from math import pi, atan2

class Player:
    def __init__(self, display, x, y):
        self.display = display

        self.surf = pg.transform.rotate(pg.image.load("assets/player.png"), -90)
        self.rect = self.surf.get_rect()
        self.deg = 0

        self.pos = pg.Vector2(x, y)
        self.speed = 7

    def rotation(self, mpos):
        adj = mpos[0] - self.pos.x
        opp = mpos[1] - self.pos.y
        rad = atan2(adj, opp)
        deg = rad * (180 / pi)

        self.new_surf = pg.transform.rotate(self.surf, deg)
        self.new_rect = self.new_surf.get_rect(center=self.pos)

    def movement(self, keys):
        if keys[pg.K_w]: self.pos.y -= self.speed
        if keys[pg.K_s]: self.pos.y += self.speed
        if keys[pg.K_a]: self.pos.x -= self.speed
        if keys[pg.K_d]: self.pos.x += self.speed

    def update(self, keys, mpos):
        self.rotation(mpos)
        self.movement(keys)
        self.display.blit(self.new_surf, self.new_rect)