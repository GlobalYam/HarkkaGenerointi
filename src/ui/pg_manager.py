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
        self.screen_res_default = pg.display.get_window_size()

        self.screen_updated = True
        self.fullscreen = False
        self.repeat = False

        self.world_shape = (5, 5)
        self.chunk_shape = (25, 25)

        self.zoom_level = 2
        self.draw_entropy = False
        self.chunk_relative_x = self.chunk_shape[1] // 2
        self.chunk_relative_y = self.chunk_shape[0] // 2
        self.render_distance = 1
        self.render_list = []
        self.skip_every_other_frame = True
        self.skip_frame = False
        self.reset()

    def reset(self):
        self.chunk_manager = node_manager(self.world_shape, (25, 25))

        # Tämä for looppi tapahtuu kahdesti dedaulttina
        for node in self.chunk_manager.chunk_list:
            if node is None:
                continue
            self.node_setup(node)
        self.update_render_list()

    def node_setup(self, node):
        if node.generate or node.level_complete or node.retired:
            return
        node.my_level = self.set_level(self.chunk_shape, 6, (3, 8))

        node.wfc_manager = wfc(node.my_level.grid, self.adjacency_rules)
        node.wfc_manager.initial_setup()
        node.generate = True

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

            if self.skip_every_other_frame:
                if self.skip_frame:
                    self.skip_frame = False
                    return
            self.screen_updated = False

            # Clear
            self.screen.fill((0, 0, 0))
            for chunk, relative_coords in self.render_list:
                self.draw_chunk_node(chunk, relative_coords)
            # Piirrä pelaaja keskelle
            # self.draw_debug((self.chunk_relative_x, self.chunk_relative_y), (0,0), 4)
            # pg.draw.rect(
            # self.screen,
            # (2 * 30, 2 * 20, 2 * 10),
            # (1, 1, 10, 10),
            # )

            pg.display.flip()

    def draw_debug(self, coordinates, chunk_offset, entity_number):
        """piirtää olion annettuihin kordinaatteihin, erottaen oliot toisistaan numeroilla"""
        font = pg.font.Font(None, int(30))
        pg.draw.line(
            self.screen,
            (entity_number * 30, entity_number * 20, entity_number * 10),
            (1, 1),
            (self.screen_w, self.screen_h),
        )
        pg.draw.line(
            self.screen,
            (entity_number * 30, entity_number * 20, entity_number * 10),
            (self.screen_w, 1),
            (1, self.screen_h),
        )
        text = font.render(
            f"x:{self.chunk_relative_x} y:{self.chunk_relative_y}", True, (255, 0, 0)
        )

        text_rect = text.get_rect(topleft=(30, 10))
        self.screen.blit(text, text_rect)

        text = font.render(
            f"x_chunk:{self.chunk_manager.current_x} y_chunk:{self.chunk_manager.current_y}",
            True,
            (255, 0, 0),
        )

        text_rect = text.get_rect(topleft=(30, 40))
        self.screen.blit(text, text_rect)

    def draw_chunk_node(self, node, relative_coordinates):
        if node != None and node.my_level != None:
            draw_based_on = node.my_level.grid
            if self.draw_entropy:
                draw_based_on = node.wfc_manager.entropy

            self.draw_chunk_from_grid(draw_based_on, relative_coordinates)
        elif node != None:
            self.draw_empty_chunk(node.coords, relative_coordinates)

    def draw_empty_chunk(self, coords, relative_coordinates=(0, 0)):
        x_chunk_offset, y_chunk_offset = relative_coordinates

        height, width = self.chunk_shape
        cell_size = (
            min(self.screen_h // height, self.screen_w // width) // self.zoom_level
        )

        # offset näytön keskelle
        offset_x = (self.screen_w - width * cell_size) // 2
        offset_y = (self.screen_h - height * cell_size) // 2

        # offset suhteellisilla kordinaateilla
        offset_x += (x_chunk_offset * width * cell_size) - (
            self.chunk_relative_x * cell_size
        )
        offset_y += (y_chunk_offset * height * cell_size) - (
            self.chunk_relative_y * cell_size
        )

        font = pg.font.Font(None, int(cell_size * 8))

        # Piirä näytölle solut
        number = (int(coords[0]) + int(coords[1])) / (self.world_shape[0] * 2)
        pg.draw.rect(
            self.screen,
            (number * 225, number * 225, number * 225),
            (
                offset_x + (width * cell_size) // 2 - cell_size // 2,
                offset_y + (width * cell_size) // 2 - cell_size // 2,
                cell_size * height,
                cell_size * width,
            ),
        )
        text = font.render(f"{(int(coords[0]), int(coords[1]))}", True, (255, 255, 255))
        text_rect = text.get_rect(
            center=(offset_x + cell_size * (height), offset_y + cell_size * height)
        )
        self.screen.blit(text, text_rect)

    def draw_chunk_from_grid(self, grid, relative_coordinates=(0, 0)):
        """Funktio joka piirtää näytölle annetun gridin"""
        x_chunk_offset, y_chunk_offset = relative_coordinates

        height, width = grid.shape
        cell_size = (
            min(self.screen_h // height, self.screen_w // width) // self.zoom_level
        )

        # offset näytön keskelle
        offset_x = (self.screen_w - width * cell_size) // 2
        offset_y = (self.screen_h - height * cell_size) // 2

        # offset suhteellisilla kordinaateilla
        offset_x += (x_chunk_offset * width * cell_size) - (
            self.chunk_relative_x * cell_size
        )
        offset_y += (y_chunk_offset * height * cell_size) - (
            self.chunk_relative_y * cell_size
        )

        font = pg.font.Font(None, int(cell_size * 0.8))

        # Piirä näytölle solut
        for y, row in enumerate(grid):
            for x, number in enumerate(row):
                screen_y = offset_y + cell_size * (y + height // 2)
                screen_x = offset_x + cell_size * (x + width // 2)

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

    def game_step(self):
        """Pyörittää yhden askeleen pelilogiikkaa, eli näppäimet, logiikka, ja näytönpäivitys"""
        self.get_input()
        self.logic_step()
        self.update_screen()

    def logic_step(self):
        """funktio joka pyörittää pygameloopin frame-to-frame logiikkaa"""
        # toista kaikille generoituville chunkeille wfc algoritmia
        temp_screen_updated = False
        for node in self.chunk_manager.chunk_list:
            if node == None or node.my_level == None:
                continue
            if not node.level_complete and node.generate:
                # print('generating')
                temp_screen_updated = True
                node.level_complete = not node.wfc_manager.step()

                # harvoissa tilanteissa, entropiaa tulee pävittää globaalisti että konfilkti ratkeaa
                if node.level_complete is False:
                    node.wfc_manager.level_entropy()
                    node.level_complete = not node.wfc_manager.step()
                    if node.level_complete is True:
                        temp_screen_updated = True
                else:
                    temp_screen_updated = True
            elif not node.retired:
                node.retired = True
                if node == self.chunk_manager.current_chunk:
                    self.update_render_list()
                    for neighbor in self.chunk_manager.set_neighbors(node.coords, 1):
                        self.node_setup(neighbor)

        if temp_screen_updated:
            self.screen_updated = True

        # Wrappaa suhteelliset kordinaatit, ja siirrä nykyistä chunkkia
        wrap = (
            (self.chunk_relative_x) // self.chunk_shape[1],
            (self.chunk_relative_y) // self.chunk_shape[0],
        )
        # print(wrap)s
        if wrap != (0, 0):
            self.chunk_relative_x, self.chunk_relative_y = (
                (self.chunk_relative_x) % self.chunk_shape[1],
                (self.chunk_relative_y) % self.chunk_shape[0],
            )
            self.chunk_manager.change_current_chunk(wrap)
            self.node_setup(self.chunk_manager.current_chunk)
            self.chunk_manager.current_chunk.retired = False
            self.update_render_list()

    def get_input(self):
        """funktio joka ottaa näppäininputit"""
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
                        self.chunk_relative_y -= 25

                    case "a":
                        # liiku vasemmalle
                        self.chunk_relative_x -= 25

                    case "s":
                        # liiku alas
                        self.chunk_relative_y += 25

                    case "d":
                        # liiku oikealle
                        self.chunk_relative_x += 25

                    case "r":
                        # resetoi taso
                        self.reset()

                    # case "f":
                    #     # fullscreen
                    #     self.screen_updated = True
                    #     if self.fullscreen is False:
                    #         pg.display.set_mode((0, 0), pg.FULLSCREEN)
                    #         self.screen_res_current = pg.display.get_window_size()
                    #         self.screen_h, self.screen_w = self.screen_res_current
                    #         self.fullscreen = True
                    #     else:
                    #         self.screen_res_current = self.screen_res_default
                    #         self.screen_h, self.screen_w = self.screen_res_current
                    #         self.display_surf = pg.display.set_mode(
                    #             self.screen_res_current
                    #         )
                    #         self.fullscreen = False

                    case "z":
                        # zoom sisään
                        if self.zoom_level < 10:
                            self.zoom_level += 1
                            self.render_distance += 1
                            self.update_render_list()

                    case "x":
                        # zoom ulos
                        if self.zoom_level > 1:
                            self.zoom_level -= 1
                            self.render_distance -= 1
                            self.update_render_list()

                self.screen_updated = True
