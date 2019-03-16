import pygame as pg

vec = pg.math.Vector2

WIDTH = 1024
HEIGHT = 768

DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
RED = (255, 0, 0)

FPS = 60
TITLE = "pyBoat"
BGCOLOR = DARKGREY

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

PLAYER_IMG = 'uBoat2.png'
MINE_IMG = 'mine2.png'
FLOOR_IMG = 'ocean2.png'
END_IMG = 'flag.png'

PLAYER_HEALTH = 1
PLAYER_SPEED = 120
PLAYER_ROT_SPEED = 100
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(20, 0)
