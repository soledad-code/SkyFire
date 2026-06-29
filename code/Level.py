#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_HEIGHT, C_WHITE, C_RED, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_PURPLE, WIN_WIDTH
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.GameOver import GameOver
from code.Player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        self.timeout = 20000 # 20 SEGUNDOS
        self.music_name = 'Level1'
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]: # MODO PARA DOIS PLAYERS
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

        # FONTE PIXEL
        self.font_path = './asset/PressStart2P-Regular.ttf'


    def run(self):
        pygame.mixer_music.load(f"./asset/{self.music_name}.wav") # ADD MÚSICA DO LEVEL
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock() # PADRONIZAÇÃO FPS

        while True:
            clock.tick(60) # FPS

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                # VERIFICAÇÃO DE TIRO
                if isinstance(ent, (Player,Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                #IMPRIMINDO VIDA
                if ent.name == 'Player1':
                    self.level_text(12, f'P1 HP:{ent.health} | SC:{ent.score}', C_GREEN, (10, 25))
                if ent.name == 'Player2':
                    self.level_text(12, f'P2 HP:{ent.health} | SC:{ent.score}', C_PURPLE, (10, 40)) # imprime o fps

            # VOLTAR AO MENU
            self.level_text(12, 'ESC - MENU', C_WHITE, (WIN_WIDTH - 125, 10))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN: # PRESSIONA ESC PARA VOLTAR AO MENU
                    if event.key == pygame.K_ESCAPE:
                        pygame.mixer_music.stop()
                        return 'menu'
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))


            # TIROS
            for ent in self.entity_list.copy():
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)

            # TEXTOS NA TELA
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 100:.1f}s', C_WHITE, (10, 5)) # tempo da fase
            self.level_text(14, f'fps: {clock.get_fps():.0f}', C_RED, (10, WIN_HEIGHT - 35)) # imprime o fps
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_RED, (10, WIN_HEIGHT - 20)) #
            pygame.display.flip()

            # COLISÕES
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            # VERIFICA SE PLAYERS MORRERAM
            players_alive = 0
            for ent in self.entity_list:
                if ent.name in ['Player1', 'Player2'] and ent.health > 0:
                    players_alive += 1

            if players_alive == 0: #TODOS MORRERAM
                pygame.mixer_music.stop()

                #PEGA PONTUAÇÃO
                player1_score = 0
                player2_score = 0
                for ent in self.entity_list:
                    if ent.name == 'Player1':
                        player1_score = ent.score
                    elif ent.name == 'Player2':
                        player2_score = ent.score

                #MOSTRA GAME OVER
                game_over = GameOver(self.window)
                if self.game_mode == MENU_OPTION[0]: #JOGADOR 1
                    game_over.run(player1_score, game_mode='1')
                else:
                    game_over.run(player1_score, player2_score, game_mode='2')
                return 'menu'

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        if os.path.exists(self.font_path):
            text_font: Font = pygame.font.Font(self.font_path, text_size)
        else:
            text_font: Font = pygame.font.SysFont('Arial', text_size)

        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(topleft=text_pos)
        self.window.blit(text_surf, text_rect)
