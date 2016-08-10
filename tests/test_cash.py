import unittest
from ..src.accounts import Cash


class CheckCash(unittest.TestCase):

    def test_creation(self):
        '''test object creation'''
        cash = Cash()
        self.assertEqual(isinstance(cash, Cash)
                         and cash is not None, True)

    def test_value(self):
        '''test that we can set value by private var'''
        cash = Cash()
        cash._value = 50
        self.assertEqual(cash.value, 50)


if __name__ == "__main__":
    unittest.main()
