import unittest
from logic.wfc import Wavefuntioncollapse as wfc
from logic.level import Level

class TestWavefuntioncollapse(unittest.TestCase):
    def setUp(self):
        height = 10
        width = 10
        
        self.test_floor_plan = Level(height, width)

        self.test_floor_plan.add_floor((3, 3), 3, 3)
        
        adjacency_rules = [
            [4,4,0,0],
            [4,3,4,2],
            [0,3,4,2],
            [0,2,1,2]
        ]
        
        self.wfc_manager = wfc(self.test_floor_plan.grid, adjacency_rules)

    def test_entropy_is_full_when_not_set(self):
        coords = 1,1

        self.assertEqual(self.wfc_manager.tile_entropy(coords), 4)
    
    def test_entropy_is_set(self):
        coords = 1,1
        self.wfc_manager.initial_setup()

        self.assertEqual(self.wfc_manager.tile_entropy(coords), 2)
    
    def test_entropy_is_zero(self):
        coords = 0,0
        self.wfc_manager.initial_setup()

        self.assertEqual(self.wfc_manager.tile_entropy(coords), 0)

    def test_invalid_get_valid_neighbors(self):
        coords = -1,-1
        self.assertEqual(self.wfc_manager.get_valid_neighbors(coords), False)

    def test_step(self):
        coords = 8,8
        self.test_floor_plan.add_floor((1, 1), 7,8)
        self.test_floor_plan.add_floor((1, 1), 8,7)

        self.wfc_manager.initial_setup()
        self.assertEqual(self.wfc_manager.tile_entropy(coords), 1)

        compleation_status = self.wfc_manager.step()

        self.assertEqual(self.wfc_manager.tile_entropy(coords), 0)
        self.assertEqual(compleation_status, True)

        compleation_status = self.wfc_manager.step()
        self.assertEqual(compleation_status, False)
    
    def test_build_room_and_floor_failed(self):
        build_status = self.test_floor_plan.add_floor((0, 0), 7,8)
        self.assertEqual(build_status, False)

        build_status = self.test_floor_plan.add_floor((1, 1), 7,8)
        self.assertEqual(build_status, True)

        build_status = self.test_floor_plan.add_room((0, 0), 7,8)
        self.assertEqual(build_status, False)

        build_status = self.test_floor_plan.add_room((5, 5), 2,2)
        self.assertEqual(build_status, False)



