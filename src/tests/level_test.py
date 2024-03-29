import unittest
from logic.level import Level


class TestFloor(unittest.TestCase):
    def setUp(self):
        pass

    def test_min_floor(self):
        height = 1
        width = 1

        test_floor_plan = Level(height, width)
        floor_as_text = str(test_floor_plan)

        self.assertEqual(floor_as_text, "[1.]\n")

    def test_room_placement(self):
        height = 10
        width = 10

        test_floor_plan = Level(height, width)

        test_floor_plan.add_room((3, 3), 5, 5)
        floor_as_text = str(test_floor_plan)

        floorplanastext = "[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]\n[1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]\n[1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]\n[1. 0. 0. 2. 2. 2. 2. 2. 0. 1.]\n[1. 0. 0. 2. 3. 3. 3. 2. 0. 1.]\n[1. 0. 0. 2. 3. 3. 3. 2. 0. 1.]\n[1. 0. 0. 2. 3. 3. 3. 2. 0. 1.]\n[1. 0. 0. 2. 2. 2. 2. 2. 0. 1.]\n[1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]\n[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]\n"

        self.assertEqual(floor_as_text, floorplanastext)
