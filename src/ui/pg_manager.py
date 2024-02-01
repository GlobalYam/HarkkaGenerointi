import numpy as np
import pygame as pg


class PygameManager:
    """Luokka joka vastaa pygamen hallinnasta"""

    def __init__(self, shape):
        "alustaa managerin näytön"
        self.screen_w, self.screen_h = shape
        self.screen = pg.display.set_mode((self.screen_w, self.screen_h))

    def draw_screen_from_grid(self, grid):
        """Funktio joka piirtää näytölle annetun gridin"""
        # Clear the screen
        self.screen.fill((0, 0, 0))
        height, width = grid.shape
        self.cell_size = min(self.screen_h // height, self.screen_w // width)

        # Draw grid and colored squares
        for y, row in enumerate(grid):
            for x, number in enumerate(row):
                screen_y = self.cell_size * y
                screen_x = self.cell_size * x

                pg.draw.rect(
                    self.screen,
                    (number * 30, number * 30, number * 30),
                    (screen_x, screen_y, self.cell_size, self.cell_size),
                )
        pg.display.flip()

        def get_input(self):
            return [event for event in pg.event.get()]
