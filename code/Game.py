#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame # importa a biblioteca pygame para criar jogos
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()  # inicializando o pygame
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # cria uma janela e guarda na variável self.window

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass




