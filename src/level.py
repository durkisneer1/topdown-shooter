import pygame as pg
from player import Player, Bullet
from enemies import Zombie
from support import import_folder
from settings import *


class Level:
    def __init__(self, display):
        self.display = display

        # one-time image imports
        self.bg_image = pg.transform.scale(pg.image.load("../assets/background/grass.png").convert(), (1600, 900))
        self.bullet_image = pg.image.load("../assets/bullet.png").convert_alpha()
        self.zombie_image_list = import_folder("../assets/zombie", 0.5)

        self.player = Player(display, WIDTH / 2, HEIGHT / 2)

        self.bullet_group = pg.sprite.Group()
        self.zombie_group = pg.sprite.Group()

        self.bullet_delay = 0
        self.can_shoot = True

        self.ZOMBIE_SPAWN = pg.USEREVENT + 1
        pg.time.set_timer(self.ZOMBIE_SPAWN, 500)

    def shooting(self, m_input, m_pos):
        if self.can_shoot:
            if m_input[0]:
                Bullet(self.display, self.bullet_group, m_pos, self.player.pos.copy(), self.bullet_image)
                self.can_shoot = False
        else:
            self.bullet_delay += 1
            if self.bullet_delay >= 10:
                self.bullet_delay = 0
                self.can_shoot = True

    def enemy_spawn(self, events):
        for ev in events:
            if ev.type == self.ZOMBIE_SPAWN:
                if len(self.zombie_group) < 20:
                    Zombie(self.display, self.zombie_group, self.zombie_image_list)

    def kill_collision(self):
        for blt in self.bullet_group:
            for zmb in self.zombie_group:
                if zmb.rect is not None:
                    if blt.rect.colliderect(zmb.rect) and pg.sprite.collide_mask(blt, zmb):
                        zmb.kill()
                        blt.kill()
                        break

    def update(self, keys, m_pos, m_input, events):
        self.shooting(m_input, m_pos)
        self.enemy_spawn(events)
        self.kill_collision()

        self.display.blit(self.bg_image, (0, 0))
        for blt in self.bullet_group:
            blt.update()
        for zmb in self.zombie_group:
            zmb.update(self.player.pos.copy())

        self.player.update(keys, m_pos)
