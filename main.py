from settings import *
from player import Player

class Game:
    def __init__(self):
        self.player = Player(screen, WIDTH / 2, HEIGHT / 2)

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
            mpos = pg.mouse.get_pos()

            screen.fill("darkgreen")
            self.player.update(keys, mpos)

            pg.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()