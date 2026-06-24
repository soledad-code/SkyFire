import os

import pygame
WIN_WIDTH = 576
WIN_HEIGHT = 324
# A


# C
COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 91, 172)
COLOR_YELLOW = (255, 255, 0)


# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0' : 0,
    'Level1Bg1' : 1,
    'Level1Bg2' : 2,
    'Level1Bg3' : 3,
    'Level1Bg4' : 4,
    'Player1' : 3,
    'Player2' : 3,
    'Enemy1': 2,
    'Enemy2': 1,
}

# F
FONT_PATH = './asset/PressStart2P-Regular.ttf'
FONT_SIZE_TITLE = 46
FONT_SIZE_SUBTITLE = 22
FONT_SIZE_INSTRUCTION = 15
FONT_SIZE_DEFAULT = 14

# M
MENU_OPTION = ("NEW GAME 1P",
               "NEW GAME 2P - COOPERATIVE",
               "NEW GAME 2P - COMPETITIVE",
               "SCORE",
               "EXIT")
MENU_BG = './asset/MenuBg.png'
MENU_SOUND = './asset/Menu.wav'

MENU_TITLE_POS = (WIN_WIDTH / 2, 80)
MENU_SUBTITLE_POS = (WIN_WIDTH / 2, 120)
MENU_INSTRUCTION_POS = (WIN_WIDTH / 2, WIN_HEIGHT - 60)

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