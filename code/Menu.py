#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Rect
from pygame.font import Font
from pygame.surface import Surface

from code.Const import WIN_WIDTH


class Menu: # define a classe Menu
    def __init__(self, window): # metodo construtor colocando a janela como parâmetro
        self.window = window # guarda a referência da janela na variável self.window para ser usada em outros métodos
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect()

    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", (255, 128, 0), ((WIN_WIDTH/2),80))
            pygame.display.flip()

            #check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit() # end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)