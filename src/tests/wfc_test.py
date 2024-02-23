import unittest
from logic.wfc import Wavefuntioncollapse as wfc
from logic.level import Level

class TestWavefuntioncollapse(unittest.TestCase):
    def setUp(self):
        pass

    def test_entropy_is_full_when_not_set(self):
        height = 10
        width = 10
        coords = 1,1
        test_floor_plan = Level(height, width)

        test_floor_plan.add_room((3, 3), 5, 5)
        
        adjacency_rules = [
            [4,4,0,0],
            [4,3,4,2],
            [0,3,4,2],
            [0,2,1,2]
        ]
        
        wfc_manager = wfc(test_floor_plan.grid, adjacency_rules)

        self.assertEqual(wfc_manager.tile_entropy(coords), 4)
    
    def test_entropy_is_set(self):
        height = 10
        width = 10
        coords = 1,1
        test_floor_plan = Level(height, width)

        test_floor_plan.add_room((3, 3), 5, 5)
        
        adjacency_rules = [
            [4,4,0,0],
            [4,3,4,2],
            [0,3,4,2],
            [0,2,1,2]
        ]
        
        wfc_manager = wfc(test_floor_plan.grid, adjacency_rules)
        wfc_manager.initial_setup()

        self.assertEqual(wfc_manager.tile_entropy(coords), 2)


