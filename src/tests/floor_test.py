import unittest
from logic.floor import Floor


class TestFloor(unittest.TestCase):
    def setUp(self):
        pass

    def test_min_floor(self):
        height = 1
        width = 1

        test_floor_plan = Floor(height, width)
        floor_as_text = str(test_floor_plan)

        self.assertEqual(floor_as_text, "[1.]\n")
