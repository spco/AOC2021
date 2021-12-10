import unittest
from .part2 import read_input, main, functional, Point, Line
import os

expected_value = 12


class Test(unittest.TestCase):
    def setUp(self):
        self.input_lines = read_input(os.path.join(os.path.dirname(__file__), 'test_input.txt'))

    def test_main(self):
        self.assertTrue(True)
        self.assertEqual(expected_value, main(self.input_lines))

    def test_line(self):
        line1 = Line(Point(0, 10), Point(10, 0))
        print(line1)
        print(line1.points())
    # def test_functional(self):
    #     self.assertTrue(True)
    #     self.assertEqual(expected_value, functional(self.input_lines))


if __name__ == '__main__':
    unittest.main()
