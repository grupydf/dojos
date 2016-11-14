# -*- coding: utf-8 -*-

import time
import pygame

SEED = [[0 for _ in range(50)] for _ in range(50)]
SEED[23][24] = SEED[24][25] = SEED[25][23] = SEED[25][24] = SEED[25][25] = 1


class Simulator(object):

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((550, 550))

    def simulate(self, seed, num_gens):
        for gen in range(num_gens):
            # draw generation matrix
            for r, row in enumerate(seed):
                for c, cell in enumerate(row):
                    # grid
                    pygame.draw.rect(self.screen, (100, 100, 100),
                                     ((11*c)-1, (11*r)-1, 12, 12))

                    # cell
                    if cell:
                        pygame.draw.rect(self.screen, (255, 255, 255),
                                         (11*c, 11*r, 10, 10))
                    else:
                        pygame.draw.rect(self.screen, (0, 0, 0),
                                         (11*c, 11*r, 10, 10))

            # display drawing on screen
            pygame.display.flip()

            time.sleep(1)


if __name__ == '__main__':
    Simulator().simulate(SEED, 5)
