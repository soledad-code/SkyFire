#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_YELLOW, WIN_HEIGHT, COLOR_WHITE, COLOR_RED
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.timeout = 20000 # 20 segundos
        self.music_name = 'Level1'

    def run(self):
        pygame.mixer_music.load(f"./asset/{self.music_name}.wav") # add musica no level
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock() # padronizando fps
        while True:
            clock.tick(60) # fps escolhido

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 100:.1f}s', COLOR_WHITE, (10, 5)) # tempo da fase
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_RED, (10,WIN_HEIGHT - 35)) # imprime o fps
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_RED, (10, WIN_HEIGHT - 20)) #
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont('Arial', text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(topleft=text_pos)
        self.window.blit(text_surf, text_rect)
        pass
