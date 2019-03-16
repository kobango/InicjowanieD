import pygame as pg
import asyncio
import data_analise
import input_data
from settings import *
from tilemap import collide_hit_rect
import threading
import time
vec = pg.math.Vector2


def collide_with_mines(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y

def collide_with_end_points(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y

class Player(pg.sprite.Sprite):

    
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(10, 0)
        self.pos = vec(x, y) * TILESIZE
        self.rot = 0
        self.last_shot = 0
        self.health = PLAYER_HEALTH
        self.rotation_speed = 0
        self.vel = vec(PLAYER_SPEED, 0).rotate(-self.rot)
        self.second_thread = threading.Thread(target = self.update_rotation_speed, args=())
        self.second_thread.start()
        
    def update_rotation_speed(self):

        while self.health is not 0:
            speed = input_data._Player__get_input_async_fast(input_data.host)
            speed = asyncio.run(speed)

            if 'Stopped' in speed:
                continue

            self.rotation_speed = data_analise.spliting(speed)

            print(self.rotation_speed)
            time.sleep(0.001)
        
    def get_keys(self):
        self.rot_speed = self.rotation_speed * PLAYER_ROT_SPEED*0.8
        self.vel = vec(PLAYER_SPEED, 0).rotate(-self.rot)
        #self.vel = vec(0, 0)
        #self.vel = vec(PLAYER_SPEED, 0).rotate(-self.rot)
        keys = pg.key.get_pressed()
        
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            #self.rot_speed = PLAYER_ROT_SPEED
            self.rotation_speed += 0.05
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            #self.rot_speed = -PLAYER_ROT_SPEED
            self.rotation_speed -= 0.05
        '''
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel = vec(PLAYER_SPEED, 0).rotate(-self.rot)
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel = vec(-PLAYER_SPEED / 2, 0).rotate(-self.rot)
        '''
    def update(self):
        self.get_keys()
        self.rot = (self.rot + self.rot_speed * self.game.dt) % 360
        self.image = pg.transform.rotate(self.game.player_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        collide_with_mines(self, self.game.mines, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_mines(self, self.game.mines, 'y')
        self.rect.center = self.hit_rect.center

        self.hit_rect.centerx = self.pos.x
        collide_with_end_points(self, self.game.end_points, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_end_points(self, self.game.end_points, 'y')
        self.rect.center = self.hit_rect.center

class Mine(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mines
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.mine_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.health = PLAYER_HEALTH

    def update(self):
        if self.health == 0:
            self.kill()

class End_Point(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.end_points
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.end_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.health = PLAYER_HEALTH

class Floor(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites,
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.floor_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
