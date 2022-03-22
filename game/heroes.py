import pygame as pg
from game.settings import Settings
from game.spritesheet import SpriteSheet


class Hero(pg.sprite.Sprite):
    def __init__(self, sprite_sheet_path, frame_width=Settings.SS_FRAME_WIDTH, frame_height=Settings.SS_FRAME_HEIGHT,
                 frames_per_row=10, rescale_factor=1, colorkey_color=pg.Color("black"),
                 x_pos=Settings.SS_FRAME_WIDTH * 1.5, y_pos=Settings.SCREEN_HEIGHT / 2, enemy=False):
        super().__init__()

        # Hero stats
        self.strength = 100
        self.health = 100  # TODO
        self.enemy = enemy



        # Sprite/animation initialization
        self.sprite_sheet_path = sprite_sheet_path
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.frames_per_row = frames_per_row
        self.colorkey_color = colorkey_color
        self.sprite_sheet = self.load_spritesheet()
        self.rescale_factor = rescale_factor
        self.frames = {"idle": self.get_frame_list(0),
                       "gesture": self.get_frame_list(1),
                       "walk": self.get_frame_list(2),
                       "attack": self.get_frame_list(3),
                       "die": self.get_frame_list(4)}
        self.frame = 0
        self.frame_count = 0
        self.hero_state = "idle"
        self.image = self.frames[self.hero_state][self.frame]
        self.rect = self.image.get_rect()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect.center = (self.x_pos, self.y_pos)



    def load_spritesheet(self):
        return SpriteSheet(self.sprite_sheet_path, self.frame_width, self.frame_height, self.frames_per_row,
                           self.colorkey_color)

    def get_frame_list(self, row=0):
        if self.sprite_sheet is None:
            raise FileNotFoundError("No sprite sheet found")
        return self.sprite_sheet.get_frame_list_from_row(row, self.rescale_factor, enemy=self.enemy)

    def update(self):
        self.frame_count += 1
        if self.frame_count >= Settings.HERO_FRAME_COOLDOWN:
            self.frame += 1
            self.frame_count = 0

        if self.frame >= len(self.frames[self.hero_state]):
            if self.hero_state == "die":
                self.frame = len(self.frames[self.hero_state]) - 1

            else:
                self.frame = 0
            # TODO: add behaviour after attack/dead

        self.image = self.frames[self.hero_state][self.frame]

    def set_hero_state(self, new_hero_state):
        self.hero_state = new_hero_state


