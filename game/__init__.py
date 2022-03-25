import enum

import pygame as pg
import sys
from enum import Enum, unique

from game.settings import Settings
from game.menu import MainMenu
from game.heroes import Hero





# TODO: THOUGHTS: mabe make every different GameState a subclass from Game?!

class Game:
    @unique
    class GameStates(Enum):
        CREDITS = -2
        SETTINGS_MENU = -1
        MAIN_MENU = 0
        MAP = 1
        BATTLE = 2


    def __init__(self):
        pg.init()

        # if game starts, it shows the main menu as first window
        self.game_state = self.GameStates.MAIN_MENU

        self.screen = pg.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
        self.clock = pg.time.Clock()

        self.all_sprites_battle = pg.sprite.Group()
        self.hero_bk = Hero("assets/hero_spritesheets_32x32/BronzeKnight.png", rescale_factor=5)
        self.enemy_orc = Hero("assets/orc_spritesheet.png", enemy=True,
                              x_pos=self.screen.get_width() - Settings.SS_FRAME_WIDTH * 1.5, rescale_factor=5)

        self.main_menu = MainMenu(self)
        self.all_sprites_battle.add(self.hero_bk, self.enemy_orc)

    def set_game_state(self, new_game_state: GameStates):
        self.game_state = new_game_state

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
        if self.game_state == self.GameStates.MAIN_MENU:
            self.main_menu.draw(self.screen)
        elif self.game_state == self.GameStates.BATTLE:
            self.screen.fill(pg.Color("white"))
            self.all_sprites_battle.draw(self.screen)

    def update(self):
        if self.game_state == self.GameStates.MAIN_MENU:
            self.main_menu.update(pg.event.get())

        elif self.game_state == self.GameStates.BATTLE:
            self.all_sprites_battle.update()


        pg.display.update()
        self.clock.tick(Settings.MAX_FPS)
