import unittest
from ..src.accounts import Debit


class CheckDebit(unittest.TestCase):

    def test_creation(self):
        '''test object creation'''
        debit = Debit()
        self.assertEqual(isinstance(debit, Debit)
                         and debit is not None, True)

    def test_value(self):
        '''test that we can set value by private var'''
        debit = Debit()
        debit.value = 50
        self.assertEqual(debit.value, 50)


if __name__ == "__main__":
    unittest.main()
