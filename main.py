import pygame as pg
from settings import *
from level import Level


class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Zombie Gunner")
        self.clock = pg.time.Clock()

        self.level = Level(self.screen)

    def run(self):
        run = True
        while run:
            events = pg.event.get()
            for ev in events:
                if ev.type == pg.QUIT or (ev.type == pg.KEYDOWN and ev.key == pg.K_ESCAPE):
                    run = False

            keys = pg.key.get_pressed()
            m_pos = pg.mouse.get_pos()
            m_input = pg.mouse.get_pressed()

            self.level.update(keys, m_pos, m_input, events)

            pg.display.flip()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
