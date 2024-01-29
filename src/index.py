import pygame as pg
from logic.level import Level

# PYGAME INIT & SCREEN
pg.init()
SCREEN_W = (pg.display.Info().current_w) // 2
SCREEN_H = (pg.display.Info().current_h) // 2

test_level = Level(15, 15)

print(test_level)

test_level.add_floor((2, 2), 5, 5)
test_level.add_floor((9, 3), 4, 4)
test_level.add_floor((6, 10), 3, 4)


print(test_level)
