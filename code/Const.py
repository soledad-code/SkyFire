import os

import pygame
WIN_WIDTH = 576
WIN_HEIGHT = 324
# A


# C
C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_RED = (255, 0, 0)
C_BLUE = (0, 91, 172)
C_YELLOW = (255, 255, 0)
C_GREEN = (0, 128, 0)
C_PURPLE = (128, 0, 128)

# E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'Level1Bg0' : 0,
    'Level1Bg1' : 1,
    'Level1Bg2' : 2,
    'Level1Bg3' : 3,
    'Level1Bg4' : 4,
    'Player1' : 3,
    'Player1Shot' : 3,
    'Player2' : 3,
    'Player2Shot' : 3,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy1Shot': 2,
    'Enemy2Shot': 5
}

ENTITY_DAMAGE = {
    'Level1Bg0' : 0,
    'Level1Bg1' : 0,
    'Level1Bg2' : 0,
    'Level1Bg3' : 0,
    'Level1Bg4' : 0,
    'Player1' : 1,
    'Player1Shot' : 25,
    'Player2' : 1,
    'Player2Shot' : 25,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 20

}

ENTITY_SCORE = {
    'Level1Bg0' : 0,
    'Level1Bg1' : 0,
    'Level1Bg2' : 0,
    'Level1Bg3' : 0,
    'Level1Bg4' : 0,
    'Player1' : 0,
    'Player1Shot' : 0,
    'Player2' : 0,
    'Player2Shot' : 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0
}

ENTITY_HEALTH = {
    'Level1Bg0' : 999,
    'Level1Bg1' : 999,
    'Level1Bg2' : 999,
    'Level1Bg3' : 999,
    'Level1Bg4' : 999,
    'Player1' : 500,
    'Player1Shot': 1,
    'Player2' : 500,
    'Player2Shot': 1,
    'Enemy1' : 70,
    'Enemy1Shot': 1,
    'Enemy2' : 50,
    'Enemy2Shot': 1

}

ENTITY_SHOT_DELAY = {
    'Player1': 50,
    'Player2': 50,
    'Enemy1': 200,
    'Enemy2': 100
}
# F
FONT_PATH = './asset/PressStart2P-Regular.ttf'
FONT_SIZE_TITLE = 46
FONT_SIZE_SUBTITLE = 22
FONT_SIZE_INSTRUCTION = 15
FONT_SIZE_DEFAULT = 14
FONT_SIZE_INSTRUCTION_SMALL = 10

# M
MENU_OPTION = ("NEW GAME 1P",
               "NEW GAME 2P - COOPERATIVE",
               "NEW GAME 2P - COMPETITIVE",
               "SCORE",
               "EXIT")
MENU_BG = './asset/MenuBg.png'
MENU_SOUND = './asset/Menu.wav'

MENU_TITLE_POS = (WIN_WIDTH / 2, 50)
MENU_SUBTITLE_POS = (WIN_WIDTH / 2, 90)
MENU_INSTRUCTION_POS = (WIN_WIDTH / 2, WIN_HEIGHT - 40)
MENU_OPTIONS_START_Y = 140
MENU_OPTIONS_SPACING = 25


# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                 'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                 'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 4000