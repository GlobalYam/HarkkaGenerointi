import numpy as np
import random

class SimpleWavefuntioncollapse:
    """Luokka joka toteuttaa annetulle numpyarraylle yksinkertaisen wavefunctioncollapse algoritmin"""

    def __init__(self, grid, adjacency_rules, level_manager) -> None:
        self.grid = grid
        self.width, self.height = grid.shape
        self.entropy = np.zeros((self.height, self.width))
        self.neighbours = [
            [[0, 0, 0, 0, 0] for x in range(self.width)]
            for y in range(self.height )
        ]
        self.allowed_options = [
            [[True, True, True, True, True] for x in range(self.width)]
            for y in range(self.height)
        ]
        self.adjacency_rules = adjacency_rules

        self.level_manager = level_manager

    def level_entropy(self):
        """Funktio joka laskee entropian koko tasolle"""
        for y, row in enumerate(self.grid):
            for x, value in enumerate(row):
                if value != 0:
                    self.propagate((x, y), int(value), False)
        
        for y, row in enumerate(self.grid):
            for x, value in enumerate(row):
                if value == 0:
                    self.tile_entropy((x, y))
        
        # print(f'self.entropy:\n {self.entropy}')
        
    def tile_entropy(self, coordinates):
        """Funktio joka laskee entropian yhdelle laatalle"""
        x, y = coordinates
        neighbour_data = self.neighbours[y][x]
        for tile, rule in enumerate(self.adjacency_rules):
            for neighbor_tile, allowed_number_of_tile in enumerate(rule):
                if int(neighbour_data[neighbor_tile]) > int(allowed_number_of_tile):
                    self.allowed_options[y][x][int(tile)] = False
        self.entropy[y, x] = sum([1 for allowed in self.allowed_options[y][x] if allowed is True])
        return self.entropy[y, x]

    def propagate(self, coordinates, value, update_entropy = True, repropagate = False):
        """päivitä ympäröivien solujen entropia"""

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
                if  0 <= yy < self.height-1 and 0 <= xx < self.width-1 
            ]

            for neighbor in valid_neighbors:
                xx, yy = neighbor
                if repropagate:
                    print(xx)
                    self.neighbours[yy][xx][value - 1] += 1
                # päivitä entropia, lähes aina käytössä, ellei aluesteta
                if update_entropy is True:
                    if self.grid[yy, xx] == 0:
                        self.tile_entropy((xx,yy))
                    elif repropagate:
                        self.propagate((xx,yy), value, True, False)

            print(x,y)
            print(len(self.neighbours))
            # katso omat vierekkäisyys säännöt ja vähennä naapurien sallittujen valintojen määrää.
            neighbour_data = self.neighbours[y][x]
            for neighbor_tile, allowed_number_of_tile in enumerate(self.adjacency_rules[value-1]):
                if int(neighbour_data[neighbor_tile]) == int(allowed_number_of_tile):
                    # kiellä kaikilta naapureilta kyseinen tile
                    for neighbor in valid_neighbors:
                        xx, yy = neighbor
                        self.allowed_options[yy][xx][int(neighbor_tile)] = False
            

    

    def step(self):
        """etsi matalin entropia, romahduta aalto matalimman entropian pisteessä, ja päivitä entropia"""
        coordinate_list = self.find_lowest_entropy()
        if coordinate_list:
            tile = random.choice(coordinate_list)
            self.collapse_wave_at(tile)
        else:
            print('all possible tiles collapsed')

    def find_lowest_entropy(self):
        """funktio joka etsii gridistä matalimman entropian"""
        non_zero_values = self.entropy[self.entropy != 0]

        if len(non_zero_values) > 0:
            min_non_zero_value = np.min(non_zero_values)
            min_non_zero_indices = np.where(self.entropy == min_non_zero_value)
            min_non_zero_coordinates = list(zip(min_non_zero_indices[1], min_non_zero_indices[0]))
        
            return min_non_zero_coordinates
        else:
            return []

    def collapse_wave_at(self, coordinates):
        """valitse annetujen kordinaattien solulle arvo"""
        x, y = coordinates
        tile_options = list([tilenum+1 for tilenum, allowed in enumerate(self.allowed_options[y][x]) if allowed is True])

        new_tile = random.choice(tile_options)
        
        self.grid[y, x] = new_tile
        print(self.level_manager.grid)

        self.entropy[y, x] = 0

        #päivitetään naapurien tiedot
        self.propagate((x, y), int(new_tile), True)
    
