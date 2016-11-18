# -*- coding: utf-8 -*-

import random
import time

import pygame

from game_test import game_of_life

SEED = [[0 for _ in range(50)] for _ in range(50)]

# Glider
SEED[23][24] = 1
SEED[24][25] = 1
SEED[25][23] = SEED[25][24] = SEED[25][25] = 1

# Glider gun
# SEED[20][30] = 1
# SEED[21][28] = SEED[21][30] = 1
# SEED[22][18] = SEED[22][19] = SEED[22][26] = SEED[22][27] = SEED[22][40] = SEED[22][41] = 1
# SEED[23][17] = SEED[23][21] = SEED[23][26] = SEED[23][27] = SEED[23][40] = SEED[23][41] = 1
# SEED[24][6]  = SEED[24][7]  = SEED[24][16] = SEED[24][22] = SEED[24][26] = SEED[24][27] = 1
# SEED[25][6]  = SEED[25][7]  = SEED[25][16] = SEED[25][20] = SEED[25][22] = SEED[25][23] = SEED[25][28] = SEED[25][30] = 1
# SEED[26][16] = SEED[26][22] = SEED[26][30] = 1
# SEED[27][17] = SEED[27][21] = 1
# SEED[28][18] = SEED[28][19] = 1

# Rich's p16
# SEED[19][20] = SEED[19][21] = SEED[19][22] = SEED[19][26] = SEED[19][27] = SEED[19][28] = 1
# SEED[20][19] = SEED[20][23] = SEED[20][25] = SEED[20][29] = 1
# SEED[21][19] = SEED[21][23] = SEED[21][25] = SEED[21][29] = 1
# SEED[22][18] = SEED[22][20] = SEED[22][21] = SEED[22][22] = SEED[22][23] = SEED[22][25] = SEED[22][26] = SEED[22][27] = SEED[22][28] = SEED[22][30] = 1
# SEED[23][18] = SEED[23][19] = SEED[23][29] = SEED[23][30] = 1
# SEED[26][22] = SEED[26][23] = SEED[26][22] = SEED[26][25] = SEED[26][26] = 1
# SEED[27][21] = SEED[27][23] = SEED[27][25] = SEED[27][27] = 1
# SEED[28][22] = SEED[28][26] = 1

# Random
# SEED = [[random.choice([0, 1]) for _ in range(50)] for _ in range(50)]


class Simulator(object):

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((550, 550))

    def draw_matrix(self, matrix):
        self.screen.fill([0, 0, 0])

        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, (255, 255, 255),
                                     (11*c, 11*r, 10, 10))

    def simulate(self, seed):
        self.draw_matrix(seed)
        pygame.display.flip()

        time.sleep(1)

        clock = pygame.time.Clock()

        while True:
            clock.tick(5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if (event.type == pygame.KEYDOWN
                        and event.key == pygame.K_ESCAPE):
                    return

            seed = game_of_life(seed)

            self.draw_matrix(seed)
            pygame.display.flip()


if __name__ == '__main__':
    Simulator().simulate(SEED)
