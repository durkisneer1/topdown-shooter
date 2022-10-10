import pygame as pg
from math import pi, atan2, cos, sin
from settings import WIDTH, HEIGHT


class Player:
    def __init__(self, display, x, y):
        self.display = display

        self.surf = pg.image.load("assets/player.png").convert_alpha()
        self.rect = self.surf.get_rect()
        self.new_surf = None
        self.new_rect = None

        self.deg = 0
        self.pos = pg.Vector2(x, y)
        self.direction = pg.Vector2()
        self.speed = 7
        self.offset = 50

    def rotation(self, m_pos):
        adj = m_pos[0] - self.pos.x
        opp = m_pos[1] - self.pos.y
        rad = atan2(adj, opp)
        deg = rad * (180 / pi) - 90

        self.new_surf = pg.transform.rotate(self.surf, deg)
        self.new_rect = self.new_surf.get_rect(center=self.pos)

    def keep_in_frame(self):
        if self.pos.x > WIDTH - self.offset:
            self.pos.x = WIDTH - self.offset
        elif self.pos.x < self.offset:
            self.pos.x = self.offset
        if self.pos.y > HEIGHT - self.offset:
            self.pos.y = HEIGHT - self.offset
        elif self.pos.y < self.offset:
            self.pos.y = self.offset

    def movement(self, keys):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.pos += self.direction * self.speed

        if keys[pg.K_w]:
            self.direction.y = -1
        elif keys[pg.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pg.K_a]:
            self.direction.x = -1
        elif keys[pg.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def update(self, keys, m_pos):
        self.rotation(m_pos)
        self.movement(keys)
        self.keep_in_frame()
        self.display.blit(self.new_surf, self.new_rect)


class Bullet(pg.sprite.Sprite):
    def __init__(self, display, group, m_pos, player_pos):
        super().__init__(group)
        self.display = display
        self.surf = None
        self.rect = None
        self.mask = None

        self.x_vel = None
        self.y_vel = None
        self.pos = player_pos
        self.speed = 20
        self.rotation(m_pos)
        self.direction(m_pos)

    def rotation(self, m_pos):
        adj = m_pos[0] - self.pos[0]
        opp = m_pos[1] - self.pos[1]
        rad = atan2(adj, opp)
        deg = rad * (180 / pi) + 180

        self.surf = pg.transform.rotate(pg.image.load("assets/bullet.png").convert_alpha(), deg)
        self.mask = pg.mask.from_surface(self.surf)
        self.rect = self.surf.get_rect(center=self.pos)

    def direction(self, mpos):
        degrees = atan2((self.pos.y - mpos[1]), (self.pos.x - mpos[0]))
        self.x_vel = cos(degrees) * self.speed
        self.y_vel = sin(degrees) * self.speed

    def movement(self):
        self.pos.x -= self.x_vel
        self.pos.y -= self.y_vel
        self.rect.center = self.pos

        if self.pos.x < 0 or self.pos.x > WIDTH:
            self.kill()
        elif self.pos.y < 0 or self.pos.y > HEIGHT:
            self.kill()

    def update(self):
        self.movement()
        self.display.blit(self.surf, self.rect)
