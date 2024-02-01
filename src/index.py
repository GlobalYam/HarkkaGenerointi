import pygame as pg
from logic.level import Level
from ui.pg_manager import PygameManager

# PYGAME INIT & SCREEN
pg.init()
SCREEN_W = (pg.display.Info().current_w) // 2
SCREEN_H = (pg.display.Info().current_h) // 2


test_level = Level(15, 15)
game_manager = PygameManager((SCREEN_W, SCREEN_H))

print(test_level)

test_level.add_floor((2, 2), 5, 5)
test_level.add_floor((9, 3), 4, 4)
test_level.add_floor((6, 10), 3, 4)


print(test_level)
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    game_manager.draw_screen_from_grid(test_level.grid)
    # game_manager.get_input()
