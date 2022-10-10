from settings import *
from level import Level


class Game:
    def __init__(self):
        self.level = Level(screen)

    def run(self):
        run = True
        while run:
            events = pg.event.get()
            for ev in events:
                if ev.type == pg.QUIT:
                    run = False
                if ev.type == pg.KEYDOWN:
                    if ev.key == pg.K_ESCAPE:
                        run = False

            keys = pg.key.get_pressed()
            m_pos = pg.mouse.get_pos()
            m_input = pg.mouse.get_pressed()

            screen.fill("darkgreen")
            self.level.update(keys, m_pos, m_input, events)

            pg.display.flip()
            clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()
