import unittest
from ..src.accounts import Savings


class CheckSavings(unittest.TestCase):

    def test_creation(self):
        '''test object creation'''
        savings = Savings()
        self.assertEqual(isinstance(savings, Savings)
                         and savings is not None, True)

    def test_value(self):
        '''test that we can set value by private var'''
        savings = Savings()
        savings.value = 50
        self.assertEqual(savings.value, 50)


if __name__ == "__main__":
    unittest.main()
