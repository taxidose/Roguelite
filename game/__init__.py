import pygame as pg
import sys

from game.settings import Settings
from game.heroes import Hero


class Game:
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
        self.clock = pg.time.Clock()

        self.all_sprites = pg.sprite.Group()
        self.hero_bk = Hero("assets/hero_spritesheets_32x32/BronzeKnight.png", rescale_factor=5)
        self.enemy_orc = Hero("assets/orc_spritesheet.png", enemy=True, x_pos=self.screen.get_width() - Settings.SS_FRAME_WIDTH * 1.5, rescale_factor=5)

        self.all_sprites.add(self.hero_bk, self.enemy_orc)

    def handle_events(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.hero_bk.set_hero_state("attack")
        elif keys[pg.K_DOWN]:
            self.hero_bk.set_hero_state("die")
        elif keys[pg.K_RIGHT]:
            self.hero_bk.set_hero_state("walk")
        elif keys[pg.K_SPACE]:
            self.hero_bk.set_hero_state("idle")

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def draw(self):
        self.screen.fill(pg.Color("white"))
        self.all_sprites.draw(self.screen)


    def update(self):
        self.all_sprites.update()
        pg.display.update()
        self.clock.tick(Settings.MAX_FPS)
