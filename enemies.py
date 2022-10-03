import pygame as pg
from random import randint
from math import pi, atan2
from support import import_folder
from settings import WIDTH, HEIGHT

class Zombie(pg.sprite.Sprite):
    def __init__(self, display, group):
        super().__init__(group)
        self.display = display
        
        self.surf_list = import_folder("assets/zombie", 0.5)
        self.rect = None

        edge = randint(0, 3)
        if edge == 0:
            self.pos = pg.Vector2(randint(0, WIDTH), 0)
        elif edge == 1:
            self.pos = pg.Vector2(0, randint(0, HEIGHT))
        elif edge == 2:
            self.pos = pg.Vector2(WIDTH, randint(0, HEIGHT))
        elif edge == 3:
            self.pos = pg.Vector2(randint(0, WIDTH), HEIGHT)

        self.slowdown = 33
        self.current_frame = 0
        self.anim_speed = 0.3

    def zombie_anim(self):
        frames = self.surf_list
        self.current_frame += self.anim_speed
        if self.current_frame >= len(frames):
            self.current_frame = 0
        
        self.surf = frames[int(self.current_frame)]
        self.rect = self.surf.get_rect()

    def movement(self, player_pos):
        self.rect.center = self.pos

        x_vel = player_pos.x - self.pos.x
        y_vel = player_pos.y - self.pos.y
        if x_vel > 100:
            x_vel = 100
        elif x_vel < -100:
            x_vel = -100
        if y_vel > 100:
            y_vel = 100
        elif y_vel < -100:
            y_vel = -100

        self.pos.x += x_vel / self.slowdown
        self.pos.y += y_vel / self.slowdown
    
    def rotation(self, player_pos):
        adj = player_pos.x - self.pos.x
        opp = player_pos.y - self.pos.y
        rad = atan2(adj, opp)
        deg = rad * (180 / pi) - 90

        self.new_surf = pg.transform.rotate(self.surf, deg)
        self.rect = self.new_surf.get_rect(center=self.pos)

    def update(self, player_pos):
        self.zombie_anim()
        self.rotation(player_pos)
        self.movement(player_pos)
        self.display.blit(self.new_surf, self.rect)