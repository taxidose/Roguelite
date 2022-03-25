import pygame_menu as pg_menu

from game.settings import Settings


class MainMenu(pg_menu.Menu):
    def __init__(self, game):
        super().__init__(height=Settings.SCREEN_HEIGHT, width=Settings.SCREEN_WIDTH, title="MainMenu",
                         theme=pg_menu.themes.THEME_BLUE)
        self.add.label("Main Menu")
        self.add.button("Play")
        self.add.button("Settings")
        self.add.button("Quit", pg_menu.events.EXIT)