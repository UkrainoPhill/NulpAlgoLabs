import unittest
from src.find_the_shortest_safe_route_in_sensor_field import *


class MyTestCase(unittest.TestCase):
    def test_given_field(self):
        result = main("../test/resources/input.txt", "../test/resources/output.txt")
        with open("../test/resources/output.txt") as output_file:
            output = output_file.read()
        self.assertEqual(int(output), 12)

    def test_empty_field(self):
        result = main("../test/resources/input_empty.txt", "../test/resources/output_empty.txt")
        with open("../test/resources/output_empty.txt") as output_file:
            output = output_file.read()
        self.assertEqual(int(output), -1)

    def test_full_field(self):
        result = main("../test/resources/input_full.txt", "../test/resources/output_full.txt")
        with open("../test/resources/output_full.txt") as output_file:
            output = output_file.read()
        self.assertEqual(int(output), 10)

    def test_zeros(self):
        result = main("../test/resources/input_zero.txt", "../test/resources/output_zero.txt")
        with open("../test/resources/output_zero.txt") as output_file:
            output = output_file.read()
        self.assertEqual(int(output), -1)


if __name__ == '__main__':
    unittest.main()
