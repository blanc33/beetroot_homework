import unittest

class Mathematician:

    @staticmethod
    def square_nums(list):
        return [i**2 for i in list]

    @staticmethod
    def remove_positives(list):
        return [i for i in list if i < 0]

    @staticmethod
    def filter_leaps(list):
        return [i for i in list if i%4 == 0]



class MathTest(unittest.TestCase):

    def setUp(self) -> None:
        self.m = Mathematician()

    def test_square(self):
        self.assertEqual(self.m.square_nums([7, 11, 5, 4]), [49, 121, 25, 16])

    def test_search_by_name(self):
        self.assertEqual(self.m.remove_positives([26, -11, -8, 13, -90]), [-11, -8, -90])

    def test_search_by_number(self):
        self.assertEqual(self.m.filter_leaps([2001, 1884, 1995, 2003, 2020]), [1884, 2020])




