import numpy as np
import pygame as pg
import sys
import random
from logic.level import Level
from logic.wfc import Wavefuntioncollapse as wfc


class PygameManager:
    """Luokka joka vastaa pygamen hallinnasta"""

    def __init__(self, shape, adjacency_rules) -> None:
        "alustaa managerin näytön"
        self.screen_w, self.screen_h = shape
        self.screen = pg.display.set_mode((self.screen_w, self.screen_h))
        self.adjacency_rules = adjacency_rules

        self.screen_updated = True
        self.repeat = False
        
        self.reset()

    def reset(self):
        self.my_level = self.set_level((25, 25), 6, (3, 8))

        self.wfc_manager = wfc(self.my_level.grid, self.adjacency_rules)
        self.wfc_manager.initial_setup()

    def set_level(self, level_size, room_count, room_size_range):

        level_width, level_height = level_size
        min_room, max_room = room_size_range

        level = Level(level_width, level_height)

        for i in range(room_count):
            room_width = random.randrange(min_room, max_room)
            room_height = random.randrange(min_room, max_room)
            x = random.randrange(2, level_width - room_width - 2)
            y = random.randrange(2, level_height - room_height - 2)
            level.add_floor((x,y), room_height, room_width)
        
        return level

    def update_screen(self):
        """päivittää näytön"""
        if self.screen_updated is True:
            self.screen_updated = False
            self.draw_screen_from_grid(self.my_level.grid)

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

    def get_input(self):

        #repeat the process
        if self.repeat:
            self.repeat = self.wfc_manager.step()
            
            # harvoissa tilanteissa, entropiaa tulee pävittää globaalisti että konfilkti ratkeaa 
            if self.repeat is False:
                self.wfc_manager.level_entropy()
                self.repeat = self.wfc_manager.step()
                if self.repeat is True:
                    self.screen_updated = True
            else:
                self.screen_updated = True

        for event in pg.event.get():
            # QUIT
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                key=pg.key.name(event.key)

                # print(key)

                match key:
                    case "q":
                        # QUIT
                        sys.exit()

                    case "u":
                        # päivitä näyttö manuaalisesti
                        self.screen_updated = True

                    case "e":
                        # visualisoi entropia
                        self.draw_screen_from_grid(self.wfc_manager.entropy)

                    case "c":
                        # collapse entropy
                        print("collapse wave")
                        self.wfc_manager.step()
                        self.screen_updated = True
                    
                    case "w":
                        # uudelleen laske tason entropioa (debug käyttöön)
                        self.wfc_manager.level_entropy()
                        self.draw_screen_from_grid(self.wfc_manager.entropy)
                    
                    case "a":
                        # autocomplete - toteuta step wfclle kunnes valmis
                        self.repeat = True
                        # self.update_screen(level_manager.grid)
                    
                    case "r":
                        # resetoi taso
                        self.reset()
                        self.screen_updated = True



