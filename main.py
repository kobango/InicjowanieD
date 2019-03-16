import pygame as pg
import sys
from os import path
from settings import *
from tilemap import *
from sprites import *
import time
import os




class Game:

    # Main Menu
    def main_menu(self):

        menu = True
        selected = "start"
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        # Game Resolution

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))

        # Text Renderer
        def text_format(message, textFont, textSize, textColor):
            newFont = pg.font.Font(textFont, textSize)
            newText = newFont.render(message, 0, textColor)

            return newText

        # Colors
        white = (255, 255, 255)
        black = (0, 0, 0)
        gray = (50, 50, 50)
        red = (255, 0, 0)
        green = (0, 255, 0)
        blue = (0, 0, 255)
        yellow = (255, 255, 0)

        # Game Fonts
        font = "VICTM___.TTF"

        # Game Framerate
        clock = pg.time.Clock()
        FPS = 30


        while menu:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        selected = "start"
                    elif event.key == pg.K_DOWN:
                        selected = "quit"
                    if event.key == pg.K_RETURN:
                        if selected == "start":
                            print("Start")
                            g.new()
                            g.run()


                        if selected == "quit":
                            pg.quit()
                            quit()

            # Main Menu UI
            self.screen.fill(gray)
            title = text_format("pyBoat", font, 90, yellow)
            if selected == "start":
                text_start = text_format("START", font, 95, white)
            else:
                text_start = text_format("START", font, 65, black)
            if selected == "quit":
                text_quit = text_format("QUIT", font, 95, white)
            else:
                text_quit = text_format("QUIT", font, 65, black)

            title_rect = title.get_rect()
            start_rect = text_start.get_rect()
            quit_rect = text_quit.get_rect()

            # Main Menu Text
            self.screen.blit(title, (WIDTH / 2 - (title_rect[2] / 2), 80))
            self.screen.blit(text_start, (WIDTH / 2 - (start_rect[2] / 2), 300))
            self.screen.blit(text_quit, (WIDTH / 2 - (quit_rect[2] / 2), 400))
            pg.display.update()
            clock.tick(FPS)
            pg.display.set_caption("Python - Pygame Simple Main Menu Selection")

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
        self.map = Map(path.join(game_folder,'test.txt'))
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.floor_img = pg.image.load(path.join(img_folder, FLOOR_IMG)).convert_alpha()
        self.floor_img = pg.transform.scale(self.floor_img, (TILESIZE, TILESIZE))
        self.mine_img = pg.image.load(path.join(img_folder, MINE_IMG)).convert_alpha()
        self.mine_img = pg.transform.scale(self.mine_img, (TILESIZE, TILESIZE))
        self.end_img = pg.image.load(path.join(img_folder, END_IMG)).convert_alpha()
        self.end_img = pg.transform.scale(self.end_img, (TILESIZE, TILESIZE))
        self.title_font = path.join(img_folder, 'ZOMBIE.TTF')


    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.floor = pg.sprite.Group()
        self.mines = pg.sprite.Group()
        self.end_points = pg.sprite.Group()

        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                Floor(self, col, row)

        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Mine(self, col, row)
                if tile == 'E':
                    End_Point(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)


        #self.player = Player(self, 32, 12)


        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        self.playing = True
        #pg.mixer_music.play(loops=-1)
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000.0
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)
        self.loose_text = False
        self.win_text = False

        hits = pg.sprite.spritecollide(self.player, self.mines, False)
        for hit in hits:
            self.player.health = 0
            Mine.health = 0
            hit.vel = vec(0, 0)
            if self.player.health == 0:
                self.loose_text = True
                # time.sleep(3)
                # self.playing = False

        hits = pg.sprite.spritecollide(self.player, self.end_points, False)
        for hit in hits:
            self.player.health = 2
            hit.vel = vec(0, 0)
            if self.player.health == 2:
                self.win_text = True

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(DARKGREY)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        if self.loose_text:
            self.draw_text("TRY AGAIN", self.title_font, 105, RED, WIDTH / 2, HEIGHT / 2, align="center")
            pg.display.flip()
            time.sleep(2)
            self.playing = False
        if self.win_text:
            self.draw_text("YOU WIN", self.title_font, 105, RED, WIDTH / 2, HEIGHT / 2, align="center")
            pg.display.flip()
            time.sleep(2)
            self.playing = False


        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_p:
                    self.paused = not self.paused

    def wait_for_key(self):
            pg.event.wait()
            waiting = True
            while waiting:
                self.clock.tick(FPS)
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        waiting = False
                        self.quit()
                    if event.type == pg.KEYUP:
                        waiting = False


g = Game()
g.main_menu()
while True:
    g.new()
    g.run()
