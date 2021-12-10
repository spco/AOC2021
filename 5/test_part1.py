import unittest
from .part1 import read_input, main, functional, interval
import os

expected_value = 5
expected_value = 11


class Test(unittest.TestCase):
    def setUp(self):
        self.input_lines = read_input(os.path.join(os.path.dirname(__file__),
                                                   'test_input2.txt'))

    def test_main(self):
        self.assertTrue(True)
        self.assertEqual(expected_value, main(self.input_lines))

    # def test_functional(self):
    #     self.assertTrue(True)
    #     self.assertEqual(expected_value, functional(self.input_lines))

    def test_interval(self):
        self.assertEqual(interval(0, 10, 5, 12), [5, 6, 7, 8, 9, 10])
        self.assertEqual(interval(5, 12, 0, 10), [5, 6, 7, 8, 9, 10])
        self.assertEqual(interval(1, 10, 10, 11), [10])
        self.assertEqual(interval(1, 10, 11, 12), [])


if __name__ == '__main__':
    unittest.main()
