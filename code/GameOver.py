#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pygame
import sys
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT, C_WHITE, C_RED, C_GREEN, C_PURPLE


class GameOver:
    def __init__(self, window):
        self.window = window
        self.font_path = './asset/PressStart2P-Regular.ttf'

        # Carrega as fontes em tamanhos menores para caber na tela
        self.font_title = self.load_font(36)  # Título menor (era 72)
        self.font_score = self.load_font(20)  # Pontuação menor (era 36)
        self.font_info = self.load_font(14)  # Instruções menor (era 24)

    def load_font(self, size):
        if os.path.exists(self.font_path):
            return pygame.font.Font(self.font_path, size)
        else:
            return pygame.font.SysFont('Arial', size)

    def run(self, player1_score: int, player2_score: int = None, game_mode: str = '1'):
        """Mostra a tela de Game Over"""

        # Fundo preto
        self.window.fill((0, 0, 0))

        # Título GAME OVER (mais compacto)
        title_surf = self.font_title.render('GAME OVER', True, C_RED)
        title_rect = title_surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 - 120))
        self.window.blit(title_surf, title_rect)

        # Pontuações
        y_pos = WIN_HEIGHT // 2 - 40

        if game_mode == '1':
            # Modo 1 jogador
            score_text = f'SCORE: {player1_score}'
            score_surf = self.font_score.render(score_text, True, C_WHITE)
            score_rect = score_surf.get_rect(center=(WIN_WIDTH // 2, y_pos))
            self.window.blit(score_surf, score_rect)
        else:
            # Modo 2 jogadores
            score1_surf = self.font_score.render(f'P1: {player1_score}', True, C_GREEN)
            score1_rect = score1_surf.get_rect(center=(WIN_WIDTH // 2, y_pos))
            self.window.blit(score1_surf, score1_rect)

            score2_surf = self.font_score.render(f'P2: {player2_score}', True, C_PURPLE)
            score2_rect = score2_surf.get_rect(center=(WIN_WIDTH // 2, y_pos + 40))
            self.window.blit(score2_surf, score2_rect)

        # Instruções
        info_text = 'ESC - MENU'
        info_surf = self.font_info.render(info_text, True, C_WHITE)
        info_rect = info_surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 80))
        self.window.blit(info_surf, info_rect)

        pygame.display.flip()

        # Aguarda o jogador pressionar ESC
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 'menu'