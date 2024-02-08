import numpy as np
import random


class SimpleWavefuntioncollapse:
    """Luokka joka toteuttaa annetulle numpyarraylle yksinkertaisen wavefunctioncollapse algoritmin"""

    def __init__(self, grid, adjacency_rules, level_manager) -> None:
        self.grid = grid
        self.width, self.height = grid.shape
        self.entropy = np.zeros((self.height, self.width))
        self.neighbours = [
            [[0, 0, 0, 0, 0] for x in range(self.width)] for y in range(self.height)
        ]
        self.allowed_options = [
            [[True, True, True, True, True] for x in range(self.width)]
            for y in range(self.height)
        ]
        self.adjacency_rules = adjacency_rules

        self.level_manager = level_manager

    def initial_setup(self):
        """Funktio joka laskee entropian koko tasolle"""
        for y, row in enumerate(self.grid):
            for x, value in enumerate(row):
                if value != 0:
                    self.propagate((x, y), int(value), False)

        for y, row in enumerate(self.grid):
            for x, value in enumerate(row):
                if value != 0:
                    self.rule_out_neighbours((x, y), int(value))

        self.level_entropy()

        # print(f'self.entropy:\n {self.entropy}')

    def level_entropy(self):
        for y, row in enumerate(self.grid):
            for x, value in enumerate(row):
                if value == 0:
                    self.tile_entropy((x, y))
        
    def tile_entropy(self, coordinates):
        """Funktio joka laskee entropian yhdelle laatalle"""
        x, y = coordinates
        neighbour_data = self.neighbours[y][x]
        if (x, y) == (5, 8):
            print(f'5,8 options: {self.allowed_options[y][x]}')
        if self.grid[y, x] != 0:
            self.entropy[y, x] = 0
            return 0
        for tile, rule in enumerate(self.adjacency_rules):
            for neighbor_tile, allowed_number_of_tile in enumerate(rule):
                if int(neighbour_data[neighbor_tile]) > int(allowed_number_of_tile):
                    
                    self.allowed_options[y][x][int(tile)] = False

        self.entropy[y, x] = sum(
            [1 for allowed in self.allowed_options[y][x] if allowed is True]
        )
        return self.entropy[y, x]

    def propagate(self, coordinates, value, update_entropy=True):
        """päivitä ympäröivien solujen entropia"""
        value = int(value)
        x, y = coordinates
        
        valid_neighbors = self.get_valid_neighbors(coordinates)

        if valid_neighbors and value != 0:
            for neighbor in valid_neighbors:
                xx, yy = neighbor
                new_value = int(self.grid[yy, xx])
                self.neighbours[yy][xx][value - 1] += 1
                # päivitä entropia, lähes aina käytössä, ellei aluesteta
                if update_entropy is True:
                    self.rule_out_neighbours((xx, yy), new_value)
                    self.tile_entropy((xx, yy))

    def rule_out_neighbours(self, coordinates, value):
        value = int(value)
        x, y = coordinates
        
        valid_neighbors = self.get_valid_neighbors(coordinates)
        if valid_neighbors and value != 0:
            # katso omat vierekkäisyys säännöt ja vähennä naapurien sallittujen valintojen määrää.
            neighbour_data = self.neighbours[y][x]
            # print(neighbour_data)

            for evaluated_tile, allowed_number_of_tile in enumerate(
                self.adjacency_rules[value - 1]
            ):
                if int(neighbour_data[evaluated_tile]) == int(allowed_number_of_tile):
                    print(f"x:{x} y:{y} not allowing neighbor: {evaluated_tile+1}")
                    print(neighbour_data)
                    print()
                    # kiellä kaikilta naapureilta kyseinen tile
                    for neighbor in valid_neighbors:
                        xx, yy = neighbor
                        self.allowed_options[yy][xx][int(evaluated_tile)] = False
                        print(self.allowed_options[yy][xx])

    def get_valid_neighbors(self, coordinates):
        x, y = coordinates

        if 0 <= y < self.height and 0 <= x < self.width:
            # etsi naapurien kordinaatit
            neighbors = [
                (x - 1, y),
                (x, y - 1),
                (x, y + 1),
                (x + 1, y),
            ]
            angle_neighbors = [
                (x + 1, y + 1),
                (x - 1, y - 1),
                (x - 1, y + 1),
                (x + 1, y - 1),
            ]

            # Filter out neighbors that are outside the boundaries
            valid_neighbors = [
                (xx, yy)
                for xx, yy in neighbors
                if 0 <= yy < self.height  and 0 <= xx < self.width
            ]
            return valid_neighbors
        else:
            return False
        
        

    def step(self):
        """etsi matalin entropia, romahduta aalto matalimman entropian pisteessä, ja päivitä entropia"""
        coordinate_list = self.find_lowest_entropy()
        if coordinate_list:
            tile = random.choice(coordinate_list)
            self.collapse_wave_at(tile)
            # tämä on hieman tehotonta, optimoidaan myöhemmin
            for neighbor in self.get_valid_neighbors(tile):
                self.tile_entropy(neighbor)
            return True
        else:
            return False

    def find_lowest_entropy(self):
        """funktio joka etsii gridistä matalimman entropian"""
        non_zero_values = self.entropy[self.entropy != 0]

        if len(non_zero_values) > 0:
            min_non_zero_value = np.min(non_zero_values)
            min_non_zero_indices = np.where(self.entropy == min_non_zero_value)
            min_non_zero_coordinates = list(
                zip(min_non_zero_indices[1], min_non_zero_indices[0])
            )

            return min_non_zero_coordinates
        else:
            return []

    def collapse_wave_at(self, coordinates):
        """valitse annetujen kordinaattien solulle arvo"""
        x, y = coordinates
        tile_options = list(
            [
                tilenum + 1
                for tilenum, allowed in enumerate(self.allowed_options[y][x])
                if allowed is True
            ]
        )
        if tile_options:
            new_tile = int(random.choice(tile_options))

            self.grid[y, x] = new_tile
            print(self.level_manager.grid)

            self.entropy[y, x] = 0

            # päivitetään naapurien tiedot
            self.propagate((x, y), new_tile, True)
            self.rule_out_neighbours((x, y), new_tile)
