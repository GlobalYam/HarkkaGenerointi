import numpy as np
from logic.level import Level as level
from logic.wfc import Wavefuntioncollapse as wfc

class NodeManager:
    """Luokka joka sisältää noodeja karttaa varten"""

    def __init__(self, world_shape, chunk_shape) -> None:
        self.world_height, self.world_width = world_shape
        self.chunk_list = [None]
        self.chunk_shape = chunk_shape
        print(len(self.chunk_list))
        self.chunk_grid = np.zeros((self.world_height, self.world_width))
        self.current_x = 2
        self.current_y = 2
        starting_coords = (self.current_x, self.current_y)
        self.starting_node = self.get_chunk_node(starting_coords, 2)
        self.current_node = self.starting_node
    
    def generate_node(self, coords, depth):
        """lisää chunkin kordinaatteihin, toistaa syvyyden verran"""
        x,y = coords
        #tarkista onko chunk olemassa
        if self.check_chunk(coords):
            placement = len(self.chunk_list)
            self.chunk_grid[y, x] = int(placement)

            node = Node(self.chunk_shape)
            self.chunk_list.append(node)
            self.set_neighbors(coords, depth)
            return node

    def check_chunk(self, coords):
        """tarkistaa onko chunk vapaa"""
        x,y = coords
        if self.chunk_grid[y, x] == 0:
            return True
        return False

    def set_neighbors(self, coords, depth):
        """asettaa nodelle naapurit, rekursiivinen generate chunkin kanssa"""
        depth -= 1
        if depth < 0:
            return False
        x, y = coords
        node_num = self.chunk_grid[y, x]
        node = self.get_chunk_node(coords, depth)
        
        left   = self.get_chunk_node(((x - 1)% self.world_width, y), depth)
        right  = self.get_chunk_node(((x + 1)% self.world_width, y), depth)
        top    = self.get_chunk_node((x, (y - 1)% self.world_height), depth)
        bottom = self.get_chunk_node((x, (y + 1)% self.world_height), depth)
        
        
    def get_chunk_node(self, coords, depth):
        """Palauta kordinaatteja vastaavan chunkin node, tai luo uusi"""
        x, y = coords

        if 0 < y < self.world_height and 0 < x < self.world_width:
            node_num = self.chunk_grid[y, x]
            if node_num == 0:
                self.generate_node(coords, depth)
                node_num = self.chunk_grid[y, x]
            node = self.chunk_list[int(node_num)]
            return node
    
    def get_renderlist(self, render_distance):
        render_list = []
        for x in range(-render_distance, render_distance+1):
            for y in range(-render_distance, render_distance+1):
                render_list.append((self.get_chunk_node((self.current_x-x, self.current_y-y), 1), (x,y)))
        return render_list


class Node:
    """Luokka joka vastaa yhtä kartan chunk-noodia"""

    def __init__(self, grid_shape) -> None:
        self.width, self.heigth = grid_shape
        self.my_level = None
        self.wfc_manager = None
        self.level_complete = False