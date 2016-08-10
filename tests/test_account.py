import unittest
from ..src.accounts import Account


class CheckAccount(unittest.TestCase):

    def test_creation(self):
        '''test object creation'''
        account = Account()
        self.assertEqual(isinstance(account, Account)
                         and account is not None, True)

    def test_value(self):
        '''test that we can set value by private var'''
        account = Account()
        account._value = 50
        self.assertEqual(account.value, 50)


if __name__ == "__main__":
    unittest.main()
