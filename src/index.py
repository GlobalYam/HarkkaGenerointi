import pygame as pg
from logic.level import Level
from logic.wfc import Wavefuntioncollapse as wfc
from ui.pg_manager import PygameManager


# PYGAME INIT & SCREEN
pg.init()
SCREEN_W = (pg.display.Info().current_w) // 2
SCREEN_H = (pg.display.Info().current_h) // 2


adjacency_rules = [
    [4,4,0,0],
    [4,3,4,2],
    [0,3,4,2],
    [0,2,1,2]
]

game_manager = PygameManager((SCREEN_W, SCREEN_H), adjacency_rules)

running = True
while running:
    game_manager.get_input()
    game_manager.update_screen()
