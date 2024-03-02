import numpy as np
import pygame as pg
import sys
import random
from logic.level import Level as level
from logic.wfc import Wavefuntioncollapse as wfc
from logic.node import Node as node
from logic.node import NodeManager as node_manager


class PygameManager:
    """Luokka joka vastaa pygamen hallinnasta"""

    def __init__(self, screen_shape, adjacency_rules) -> None:
        "alustaa managerin näytön"
        self.screen_w, self.screen_h = screen_shape
        self.screen = pg.display.set_mode((self.screen_w, self.screen_h))
        self.adjacency_rules = adjacency_rules

        self.screen_updated = True
        self.repeat = False

        self.chunk_shape = (5,5)

        self.zoom_level = 2
        self.draw_entropy = False
        self.relative_x = 0
        self.relative_y = 0
        self.render_distance = 1
        self.render_list = []
        self.reset()

    def reset(self):
        self.chunk_manager = node_manager(self.chunk_shape, (25, 25))
        chunk_shape = self.chunk_manager.chunk_shape

        # Tämä for looppi tapahtuu kahdesti dedaulttina
        for node in self.chunk_manager.chunk_list:
            if node is None:
                continue
            node.my_level = self.set_level(chunk_shape, 6, (3, 8))

            node.wfc_manager = wfc(node.my_level.grid, self.adjacency_rules)
            node.wfc_manager.initial_setup()
        self.update_render_list()
    
    def update_render_list(self):
        self.render_list = self.chunk_manager.get_renderlist(self.render_distance)

    def set_level(self, level_size, room_count, room_size_range):

        level_width, level_height = level_size
        min_room, max_room = room_size_range

        my_level = level(level_width, level_height)

        for i in range(room_count):
            room_width = random.randrange(min_room, max_room)
            room_height = random.randrange(min_room, max_room)
            x = random.randrange(2, level_width - room_width - 2)
            y = random.randrange(2, level_height - room_height - 2)
            my_level.add_floor((x, y), room_height, room_width)

        return my_level

    def update_screen(self):
        """päivittää näytön"""
        if self.screen_updated is True:
            self.screen_updated = False

            # Clear
            self.screen.fill((0, 0, 0))
            for chunk, relative_coords in self.render_list:
                self.draw_chunk_node(chunk, relative_coords)

            pg.display.flip()
    
    def draw_chunk_node(self, node, relative_coordinates):
        if node != None:
            draw_based_on = node.my_level.grid
            if self.draw_entropy:
                draw_based_on = node.wfc_manager.entropy

            self.draw_chunk_from_grid(draw_based_on, relative_coordinates)
        


    def draw_chunk_from_grid(self, grid, relative_coordinates = (0,0)):
        """Funktio joka piirtää näytölle annetun gridin"""
        x_chunk_offset, y_chunk_offset = relative_coordinates
        
        
        height, width = grid.shape
        cell_size = min(self.screen_h // height, self.screen_w // width) // self.zoom_level

        # offset näytön keskelle
        offset_x = (self.screen_w - width * cell_size) // 2
        offset_y = (self.screen_h - height * cell_size) // 2

        # offset suhteellisilla kordinaateilla
        chunk_height, chunk_width = self.chunk_shape
        offset_x += (x_chunk_offset*chunk_width*cell_size*5)+(self.relative_x*cell_size)
        offset_y += (y_chunk_offset*chunk_height*cell_size*5)+(self.relative_y*cell_size)

        font = pg.font.Font(None, int(cell_size * 0.8))

        # Piirä näytölle solut
        for y, row in enumerate(grid):
            for x, number in enumerate(row):
                screen_y = offset_y + cell_size * y
                screen_x = offset_x + cell_size * x

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
        


    def get_input(self):

        # repeat the process of generation for all nodes that need to generate
        temp_screen_updated = False
        for node in self.chunk_manager.chunk_list:
            if node == None:
                continue
            if not node.level_complete:
                temp_screen_updated = True
                node.level_complete = node.wfc_manager.step()

                # harvoissa tilanteissa, entropiaa tulee pävittää globaalisti että konfilkti ratkeaa
                if node.level_complete is False:
                    node.wfc_manager.level_entropy()
                    node.level_complete = node.wfc_manager.step()
                    if node.level_complete is True:
                        temp_screen_updated = True
                else:
                    temp_screen_updated = True
        if temp_screen_updated:
            self.screen_updated = True

        for event in pg.event.get():
            # QUIT
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                key = pg.key.name(event.key)

                print(key)

                match key:
                    case "q":
                        # QUIT
                        sys.exit()

                    case "u":
                        # päivitä näyttö manuaalisesti
                        self.screen_updated = True

                    case "e":
                        # visualisoi entropia
                        self.draw_entropy = not self.draw_entropy
                        # self.draw_chunk_from_grid(self.wfc_manager.entropy)

                    case "c":
                        # collapse entropy
                        # print("collapse wave")
                        # self.wfc_manager.step()
                        # self.screen_updated = True
                        pass

                    case "w":
                        # liiku ylös
                        self.relative_y += 1

                    case "a":
                        # liiku vasemmalle
                        self.relative_x += 1
                    
                    case "s":
                        # liiku alas
                        self.relative_y -= 1

                    case "d":
                        # liiku oikealle
                        self.relative_x -= 1

                    case "r":
                        # resetoi taso
                        self.reset()
                    
                    case "z":
                        # zoom sisään
                        if self.zoom_level < 10:
                            self.zoom_level += 0.05
                    
                    case "x":
                        # zoom ulos
                        if self.zoom_level > 1:
                            self.zoom_level -= 0.05

                self.screen_updated = True
