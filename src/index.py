import pygame as pg
from logic.floor import Floor

# PYGAME INIT & SCREEN
pg.init()
SCREEN_W = (pg.display.Info().current_w) // 2
SCREEN_H = (pg.display.Info().current_h) // 2

test_floor = Floor(10, 10)

print(test_floor)

test_floor.add_room((3, 3), 4, 4)

print(test_floor)
