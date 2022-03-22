import pygame as pg
from game.settings import Settings


class SpriteSheet:
    def __init__(self, sprite_sheet_path, frame_width=Settings.SS_FRAME_WIDTH, frame_height=Settings.SS_FRAME_HEIGHT,
                 frames_per_row=10, colorkey_color=pg.Color("yellow")):
        self.sheet = pg.image.load(sprite_sheet_path).convert_alpha()
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.colorkey_color = colorkey_color
        self.frames_per_row = frames_per_row

    def get_frame_list_from_row(self, row, rescale_factor, enemy):
        frame_list = []
        for frame in range(self.frames_per_row):
            sprite = pg.Surface((self.frame_width, self.frame_height)).convert_alpha()
            sprite.blit(self.sheet, (0, 0), (
                (self.frame_width * frame), (self.frame_height * row), self.frame_width, self.frame_height))
            sprite = pg.transform.scale(
                sprite, (self.frame_width * rescale_factor, self.frame_height * rescale_factor))
            if enemy:
                sprite = pg.transform.flip(sprite, flip_x=True, flip_y=False)
            sprite.set_colorkey(self.colorkey_color)
            frame_list.append(sprite)

        return frame_list

        # sprite = pg.Surface((self.frame_width, self.frame_height))
        # sprite.blit(self.sheet, (0, 0), (x, y, self.frame_width, self.frame_height))

        # def get_one_frame(self, frame_number, row=0, rescale_factor=1):
        #     image = pg.Surface((self.frame_width, self.frame_height)).convert_alpha()
        #     image.blit(self.sheet, (0, 0), ((self.frame_width * frame_number), (self.frame_height * row), self.frame_width, self.frame_height))
        #     image = pg.transform.scale(
        #         image, (self.frame_width * rescale_factor, self.frame_height * rescale_factor))
        #     image.set_colorkey(self.colorkey_color)
        #
        #     return image
        #
        # def create_animation_list(self, row, frames_per_row, rescale_factor=1):
        #     return [self.get_one_frame(frame, row, rescale_factor) for frame in range(frames_per_row)]

        # def animate_row(self, animation_list, current_index, last_update: pg.time, animation_cooldown):
        #     if self.image is None or animation_list is None:
        #         raise TypeError("Couldn't animate row, because there is no image.")
        #
        #     frame = 0
        #     current_time = pg.time.get_ticks()
        #     if current_time - last_update >= animation_cooldown:
        #         frame += 1
        #
        #         if frame >= len(animation_list):
        #             frame = 0
        #
