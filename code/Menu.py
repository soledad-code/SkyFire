#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import pygame
from pygame import Rect
from pygame.font import Font
from pygame.surface import Surface
from code.Const import (MENU_BG, MENU_SOUND, FONT_SIZE_TITLE, C_ORANGE, MENU_TITLE_POS, FONT_SIZE_SUBTITLE,
                        MENU_SUBTITLE_POS,
                        WIN_WIDTH, C_RED, MENU_OPTION, FONT_SIZE_INSTRUCTION, MENU_INSTRUCTION_POS,
                        FONT_SIZE_INSTRUCTION_SMALL, MENU_OPTIONS_START_Y)


class Menu: # define a classe Menu
    def __init__(self, window): # metodo construtor colocando a janela como parâmetro
        self.window = window # guarda a referência da janela na variável self.window para ser usada em outros métodos
        self.surf = pygame.image.load(MENU_BG).convert_alpha()
        self.rect = self.surf.get_rect()
        self.font_path = './asset/PressStart2P-Regular.ttf' # carrega fonte pixelart
        self.pixel_font = self.load_pixel_font()

    def load_pixel_font(self):
        if os.path.exists(self.font_path):
            return pygame.font.Font(self.font_path, 24)
        else:
            print(f"Fonte não encontrada '{self.font_path}'! Usando fonte padrão")
            return pygame.font.SysFont('Arial', 24)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load(MENU_SOUND)
        pygame.mixer_music.play(-1) # toca musica em loop

        while True:
            # DESENHA IMAGENS
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(FONT_SIZE_TITLE, "SKYFIRE", C_RED, MENU_TITLE_POS)
            self.menu_text(FONT_SIZE_SUBTITLE, "MOUNTAIN WAR", C_RED, MENU_SUBTITLE_POS)

            # INSTRUÇÕES DO JOGO
            for i in range(len(MENU_OPTION)):
                y_pos = MENU_OPTIONS_START_Y + (25 * i)  # 25 é o espaçamento
                if i == menu_option:
                    self.menu_text(FONT_SIZE_INSTRUCTION, MENU_OPTION[i], C_ORANGE, (WIN_WIDTH / 2, y_pos))
                else:
                    self.menu_text(FONT_SIZE_INSTRUCTION, MENU_OPTION[i], C_RED, (WIN_WIDTH / 2, y_pos))

            # Instruções no final da tela (fonte menor)
            self.menu_text(10, "RIGHT CTRL - SHOOT", C_ORANGE, MENU_INSTRUCTION_POS)
            self.menu_text(10, "SETAS - MOVE", C_ORANGE, (MENU_INSTRUCTION_POS[0], MENU_INSTRUCTION_POS[1] + 15))

            pygame.display.flip()

            # checa por todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit() # encerra pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP: # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: # selecionar
                        return MENU_OPTION[menu_option]


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        #renderiza o texto com pixelart
        if os.path.exists(self.font_path):
            text_font: Font = pygame.font.Font(self.font_path, text_size)
        else:
            text_font = pygame.font.SysFont('Arial', text_size) # suporte a falhas na disponibilidade da fonte

        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)