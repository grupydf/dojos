# -*- coding: utf-8 -*-

import time

import pygame

from game_test import game_of_life

SEED = [[0 for _ in range(50)] for _ in range(50)]
SEED[23][24] = SEED[24][25] = SEED[25][23] = SEED[25][24] = SEED[25][25] = 1


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
