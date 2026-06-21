import os

import pygame

# CORES
COLOR_ORANGE = (255, 128, 0)

# CONFIGURAÇÃO DE TELA
WIN_WIDTH = 576
WIN_HEIGHT = 324

# FONTES
FONT_PATH = './asset/PressStart2P-Regular.ttf'
FONT_SIZE_TITLE = 56
FONT_SIZE_SUBTITLE = 32
FONT_SIZE_INSTRUCTION = 20
FONT_SIZE_DEFAULT = 24

# MENU
MENU_TITLE_POS = (WIN_WIDTH / 2, 120)
MENU_SUBTITLE_POS = (WIN_WIDTH / 2, 180)
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
