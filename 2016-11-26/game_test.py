# -*- coding: utf-8 -*-

SEED = [[0 for _ in range(50)] for _ in range(50)]
SEED[23][24] = SEED[24][25] = SEED[25][23] = SEED[25][24] = SEED[25][25] = 1


def cell_check(section):
    neighbours = 0
    center = section[1][1]

    for row in section:
        for cell in row:
            neighbours += cell

    neighbours -= center

    if neighbours <= 1:
        center = 0
    elif neighbours == 3:
        center = 1
    elif neighbours >= 4:
        center = 0

    return center


def get_section(matrix, row, col):
    section = [[0 for _ in range(3)] for _ in range(3)]

    for sec_r, r in enumerate(range(row-1, row+2)):
        for sec_c, c in enumerate(range(col-1, col+2)):
            if r >= 0 and c >= 0 and r < 50 and c < 50:
                section[sec_r][sec_c] = matrix[r][c]

    return section


def game_of_life(seed):
    next_gen = [[0 for _ in range(50)] for _ in range(50)]

    for r, row in enumerate(seed):
        for c, col in enumerate(row):
            next_gen[r][c] = cell_check(get_section(seed, r, c))

    return next_gen
