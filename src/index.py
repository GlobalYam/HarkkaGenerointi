import pygame as pg
from logic.level import Level
from logic.wavefunctioncollapse import SimpleWavefuntioncollapse as swfc
from ui.pg_manager import PygameManager


# PYGAME INIT & SCREEN
pg.init()
SCREEN_W = (pg.display.Info().current_w) // 2
SCREEN_H = (pg.display.Info().current_h) // 2

adjacency_rules = [
    [2, 2, 1, 2, 2],
    [2, 4, 0, 2, 0],
    [2, 0, 2, 2, 0],
    [2, 1, 1, 0, 0],
    [4, 0, 0, 0, 4],
]

test_level = Level(15, 15)

wfc_manager = swfc(test_level.grid, adjacency_rules, test_level)
game_manager = PygameManager((SCREEN_W, SCREEN_H))
print(test_level)

test_level.add_floor((2, 2), 5, 5)
test_level.add_floor((9, 3), 4, 4)
test_level.add_floor((6, 10), 3, 4)
test_level.grid[7, 5] = 4

wfc_manager.level_entropy()

# for y, row in enumerate(wfc_manager.neighbours):
#     for x, neighbours_at_xy in enumerate(row):
#         if neighbours_at_xy != [0, 0, 0, 0, 0] and test_level.grid[y,x] == 0 and wfc_manager.entropy[y,x] == 5:
#             print(f'outliers (x,y):{x,y} {neighbours_at_xy}, entropy: {wfc_manager.entropy[y,x]}' )

# print(f'12, 7: {wfc_manager.neighbours[7][12]}, entropy: {wfc_manager.entropy[7,12]}' )
# print(f'11, 7: {wfc_manager.neighbours[7][11]}, entropy: {wfc_manager.entropy[7,11]}' )
# print(f'10, 7: {wfc_manager.neighbours[7][10]}, entropy: {wfc_manager.entropy[7,10]}' )
# print(f'9, 7: {wfc_manager.neighbours[7][9]}, entropy: {wfc_manager.entropy[7,9]}' )


print(test_level)
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    game_manager.update_screen(test_level.grid)
    game_manager.get_input(wfc_manager)
