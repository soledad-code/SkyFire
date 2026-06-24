import os

import pygame

# CORES
COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 91, 172)
COLOR_YELLOW = (255, 255, 0)

# CONFIGURAÇÃO DE TELA
WIN_WIDTH = 576
WIN_HEIGHT = 324

# MENU INICIAL
MENU_OPTION = ("NEW GAME 1P",
               "NEW GAME 2P - COOPERATIVE",
               "NEW GAME 2P - COMPETITIVE",
               "SCORE",
               "EXIT")

# VELOCIDADE
ENTITY_SPEED = {
    'Level1Bg0' : 0,
    'Level1Bg1' : 1,
    'Level1Bg2' : 2,
    'Level1Bg3' : 3,
    'Level1Bg4' : 6
}

# FONTES
FONT_PATH = './asset/PressStart2P-Regular.ttf'
FONT_SIZE_TITLE = 46
FONT_SIZE_SUBTITLE = 22
FONT_SIZE_INSTRUCTION = 15
FONT_SIZE_DEFAULT = 14

# MENU
MENU_TITLE_POS = (WIN_WIDTH / 2, 80)
MENU_SUBTITLE_POS = (WIN_WIDTH / 2, 120)
MENU_INSTRUCTION_POS = (WIN_WIDTH / 2, WIN_HEIGHT - 60)


# FUNÇÃO CARREGAR FONTE
def load_pixel_font(size: int = FONT_SIZE_DEFAULT) -> pygame.font.Font:
    if os.path.exists(FONT_PATH):
        return pygame.font.Font(FONT_PATH, size)
    else:
        print(f"Font not exist em '{FONT_PATH}'! Usando fonte padrão.")
        return pygame.font.SysFont('Arial', size)

#ASSETS
MENU_BG = './asset/MenuBg.png'
MENU_SOUND = './asset/Menu.wav'
