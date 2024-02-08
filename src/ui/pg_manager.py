import numpy as np
import pygame as pg
import sys


class PygameManager:
    """Luokka joka vastaa pygamen hallinnasta"""

    def __init__(self, shape) -> None:
        "alustaa managerin näytön"
        self.screen_w, self.screen_h = shape
        self.screen = pg.display.set_mode((self.screen_w, self.screen_h))
        self.screen_updated = True

    def update_screen(self, grid):
        if self.screen_updated == True:
            self.screen_updated = False
            self.draw_screen_from_grid(grid)

    def draw_screen_from_grid(self, grid):
        """Funktio joka piirtää näytölle annetun gridin"""
        # Clear the screen
        self.screen.fill((0, 0, 0))
        height, width = grid.shape
        cell_size = min(self.screen_h // height, self.screen_w // width)

        font = pg.font.Font(None, int(cell_size * 0.8))

        # Draw grid and colored squares
        for y, row in enumerate(grid):
            for x, number in enumerate(row):
                screen_y = cell_size * y
                screen_x = cell_size * x

                pg.draw.rect(
                    self.screen,
                    (number * 30, number * 30, number * 30),
                    (screen_x, screen_y, cell_size, cell_size),
                )
                text = font.render(str(int(number)), True, (255, 255, 255))
                text_rect = text.get_rect(
                    center=(screen_x + cell_size // 2, screen_y + cell_size // 2)
                )
                self.screen.blit(text, text_rect)
        pg.display.flip()

    def get_input(self, wfc_manager, level_manager):
        for event in pg.event.get():
            # QUIT
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                match event.key:
                    case pg.K_q:
                        # QUIT
                        sys.exit()

                    case pg.K_u:
                        # päivitä näyttö manuaalisesti
                        self.screen_updated = True

                    case pg.K_e:
                        # visualisoi entropia
                        self.draw_screen_from_grid(wfc_manager.entropy)

                    case pg.K_c:
                        # collapse entropy
                        print("collapse wave")
                        wfc_manager.step()
                        self.screen_updated = True
                    
                    case pg.K_w:
                        # uudelleen laske tason entropioa (debug käyttöön)
                        wfc_manager.level_entropy()
                        self.draw_screen_from_grid(wfc_manager.entropy)
                    
                    case pg.K_a:
                        # autocomplete - toteuta step wfclle kunnes valmis
                        repeat = True
                        while repeat:
                            repeat = wfc_manager.step()
                            self.screen_updated = True
                            # self.update_screen(level_manager.grid)
                    
                    case pg.K_r:
                        # resetoi taso
                        pass


