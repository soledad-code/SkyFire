#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame # importa a biblioteca pygame para criar jogos
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()  # inicializando o pygame
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # cria uma janela e guarda na variável self.window

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'Level1Bg', menu_return)
                level_return = level.run()
            elif menu_return in MENU_OPTION[4]:
                pygame.quit() # fecha a janela
                quit() # fecha pygame
            else:
                pass