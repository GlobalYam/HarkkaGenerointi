import numpy as np


class SimpleWavefuntioncollapse:
    """Luokka joka toteuttaa annetulle numpyarraylle yksinkertaisen wavefunctioncollapse algoritmin"""

    def __init__(self, grid, adjacency_rules) -> None:
        self.grid = grid
        self.width, self.height = grid.shape
        self.entropy = np.zeros((self.height, self.width, len(adjacency_rules) + 1))
        self.neighbours = [
            [[0, 0, 0, 0, 0] for i in range(self.width - 1)]
            for j in range(self.height - 1)
        ]
        self.adjacency_rules = adjacency_rules

        print(self.neighbours)

        self.level_entropy()

        print(self.neighbours)

    def level_entropy(self):
        """Funktio joka laskee entropian koko tasolle"""
        for y, row in enumerate(self.grid):
            for x, value in enumerate(row):
                print(value)
                if value != 0:
                    self.propagate((x, y), int(value))

    def propagate(self, coordinates, value):
        """päivitä ympäröivien solujen entropia"""

        x, y = coordinates

        if 0 <= x < self.height and 0 <= y < self.width:
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
                (i, j)
                for i, j in neighbors
                if self.grid[i, j] == 0 and 0 <= i < self.height and 0 <= j < self.width
            ]

            for neighbor in valid_neighbors:
                x, y = neighbor
                self.neighbours[y][x][value - 1] += 1

        pass

    def update_entropy(self):
        """tarkista ympäroivät naapurit"""
        pass

    def find_lowest_entropy(self):
        """funktio joka etsii gridistä matalimman entropian"""
