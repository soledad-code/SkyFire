#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame # importa a biblioteca pygame para criar jogos

from code.Menu import Menu # importa a classe Menu do arquivo Menu.py dentro da pasta code
from code.Const import WIN_WIDTH, WIN_HEIGHT

class Game:
    def __init__(self):
        pygame.init()  # inicializando o pygame
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # cria uma janela e guarda na variável self.window

    def run(self):
        while True:
            menu = Menu(self.window) # cria um novo objeto Menu a cada iteração do loop, passando a janela como parâmetro
            menu.run() # chama o metodo run do objeto Menu
            pass

            # Check for all events
            #for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #        pygame.quit()  # Close Window
            #        quit()  # end pygame



