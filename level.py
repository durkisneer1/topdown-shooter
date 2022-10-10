import pygame as pg
from player import Player, Bullet
from enemies import Zombie
from settings import WIDTH, HEIGHT


class Level:
    def __init__(self, display):
        self.display = display

        self.player = Player(display, WIDTH / 2, HEIGHT / 2)

        self.bullet_group = pg.sprite.Group()
        self.zombie_group = pg.sprite.Group()

        self.bullet_delay = 0

        self.ZOMBIE_SPAWN = pg.USEREVENT + 1
        pg.time.set_timer(self.ZOMBIE_SPAWN, 750)

    def shooting(self, minput, mpos):
        if minput[0]:
            self.bullet_delay += 1
            if self.bullet_delay >= 15:
                Bullet(self.display, self.bullet_group, mpos, self.player.pos.copy())
                self.bullet_delay = 0

    def enemy_spawn(self, events):
        for ev in events:
            if ev.type == self.ZOMBIE_SPAWN:
                Zombie(self.display, self.zombie_group)

    def kill_collision(self):
        for blt in self.bullet_group:
            for zmb in self.zombie_group:
                if zmb.rect is not None:
                    if (blt.rect.colliderect(zmb.rect) and
                    pg.sprite.collide_mask(blt, zmb)):
                        zmb.kill()
                        blt.kill()
                        break

    def update(self, keys, mpos, minput, events):
        self.shooting(minput, mpos)
        self.enemy_spawn(events)
        self.kill_collision()

        for blt in self.bullet_group:
            blt.update()
        for zmb in self.zombie_group:
            zmb.update(self.player.pos.copy())

        self.player.update(keys, mpos)
