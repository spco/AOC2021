import unittest
from .part1 import read_input, main, functional
import os

expected_value = 198


class Test(unittest.TestCase):
    def setUp(self):
        self.input_lines = read_input(os.path.join(os.path.dirname(__file__), 'test_input.txt'))

    def test_main(self):
        self.assertTrue(True)
        self.assertEqual(expected_value, main(self.input_lines))

    def test_functional(self):
        self.assertTrue(True)
        self.assertEqual(expected_value, functional(self.input_lines))


if __name__ == '__main__':
    unittest.main()
