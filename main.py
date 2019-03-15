import pygame as pg
import sys
from os import path
from settings import *
from tilemap import *
from sprites import *




class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()

    def draw_text(self, text, font_name, size, color, x, y, align="nw"):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "nw":
            text_rect.topleft = (x, y)
        if align == "ne":
            text_rect.topright = (x, y)
        if align == "sw":
            text_rect.bottomleft = (x, y)
        if align == "se":
            text_rect.bottomright = (x, y)
        if align == "n":
            text_rect.midtop = (x, y)
        if align == "s":
            text_rect.midbottom = (x, y)
        if align == "e":
            text_rect.midright = (x, y)
        if align == "w":
            text_rect.midleft = (x, y)
        if align == "center":
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'textures')
        #self.title_font = path.join(img_folder, 'ZOMBIE.TTF')
        self.map = Map(path.join(game_folder, 'MAPA.txt'))
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.floor_img = pg.image.load(path.join(img_folder, FLOOR_IMG)).convert_alpha()
        self.floor_img = pg.transform.scale(self.floor_img, (TILESIZE, TILESIZE))

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.floor = pg.sprite.Group()

        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                Floor(self, col, row)

        self.player = Player(self, 32, 35)

        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Mine(self, col, row)

        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        self.playing = True
        #pg.mixer_music.play(loops=-1)
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000.0
            self.events()


g = Game()
while True:
    g.new()
    g.run()
