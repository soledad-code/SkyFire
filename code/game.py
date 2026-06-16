#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame # importa a biblioteca pygame para criar jogos
from code.menu import Menu # importa a classe Menu do arquivo menu.py dentro da pasta code

class Game:
    def __init__(self):
        pygame.init()  # inicializando o pygame
        self.window = pygame.display.set_mode(size=(600, 480))  # cria uma janela e guarda na variável self.window

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



