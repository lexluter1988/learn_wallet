import unittest
from ..src.accounts import Credit


class CheckCredit(unittest.TestCase):

    def test_creation(self):
        '''test object creation'''
        credit = Credit()
        self.assertEqual(isinstance(credit, Credit)
                         and credit is not None, True)

    def test_value(self):
        '''test that we can set value by setter
        and it is negative for credit'''
        credit = Credit(True)
        credit.value = 50
        self.assertEqual(credit.value, -50)

    # cannot fully understand how to assert setter
    # which is not method for 'assertEqual'
    # def test_incorrect_value(self):
    #     self.account = Cash()
    #     self.assertRaises(NotMoneyError, )

    def test_clean_status_before(self):
        '''test that account is clean before assigment'''
        credit = Credit(True)
        self.assertEqual(credit.clean, True)

    def test_clean_status_after(self):
        '''test that account is not clean after assigment'''
        credit = Credit(True)
        credit.value = 50
        self.assertEqual(credit.clean, False)

if __name__ == "__main__":
    unittest.main()
