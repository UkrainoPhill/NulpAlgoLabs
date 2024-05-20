import unittest
from src.beers import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        main("../test/resources/input_beers.txt", "../test/resources/output_beers.txt")
        with open("../test/resources/output_beers.txt") as output_file:
            output = output_file.read()
        self.assertEqual(int(output), 2)

    def test_small(self):
        main("../test/resources/input_beers_small.txt", "../test/resources/output_beers_small.txt")
        with open("../test/resources/output_beers_small.txt") as output_file:
            output = output_file.read()
        self.assertEqual(int(output), 2)

    def test_big(self):
        main("../test/resources/input_beers_big.txt", "../test/resources/output_beers_big.txt")
        with open("../test/resources/output_beers_big.txt") as output_file:
            output = output_file.read()
        self.assertEqual(int(output), 2)

    def test_one_beer(self):
        main("../test/resources/input_beers_one_beer.txt", "../test/resources/output_beers_one_beer.txt")
        with open("../test/resources/output_beers_one_beer.txt") as output_file:
            output = output_file.read()
        self.assertEqual(int(output), 1)


if __name__ == '__main__':
    unittest.main()
