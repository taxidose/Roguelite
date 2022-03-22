import pygame as pg
from game.constants import Constants


class Room:
    pass


class RoomSprites(pg.sprite.Sprite):
    def __init__(self, offset=0):
        super().__init__()
        self.offset = offset
