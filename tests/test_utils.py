import unittest
from ..src.utils import Parsers

new_account_wrong_values = ('new_account',
                            'bekrtlbnflk',
                            '33453553',
                            'new_',
                            'new_account name',
                            'new_account name=alexey 124',)


open_account_wrong_values = ('new_account',
                             'bekrtlbnflk',
                             '33453553',
                             'open_account_',
                             'open_account name=   ',
                             '1234 ***lexey 124',)


history_wrong_values = ('12-*-* unt',
                        'bnflk',
                        '33453553',
                        'history_',
                        'history=1',
                        'history name=1243',
                        'history records=test',)

payments_wrong_values = ('12-*-* unt',
                         'bnflk',
                         '33453553',
                         'payments_',
                         'pay=1',
                         'payments records= 21344564466',
                         'payments records=test',)

income_wrong_values = ('income dshit',
                       'income 1000',
                       '23345',
                       'income category=cash value=,',
                       'income category=cash value=100 comment  = 13445',)

withdraw_wrong_values = ('income dshit',
                         'withdraw 1000',
                         '23345',
                         'withdraw category=credit value=ert100,',
                         'withdraw value=100 category=cash value=100 c 135',)

wrong_pay_values = ('pay',
                    'pay credit 1000',
                    'pay category=cash value',
                    'payment category=cash value=100',)

wrong_debug_values = ('ofn',
                      '124',
                      'debuggg',
                      'debug=on',
                      'bgg',)


class CheckParsers(unittest.TestCase):

    def test_creation(self):
        '''test object creation'''
        parser = Parsers()
        self.assertEqual(isinstance(parser, Parsers)
                         and parser is not None, True)

    def test_new_account_check_for_wrong_values(self):
        '''test that all wrong input will be filtered'''
        parser = Parsers()
        for i in new_account_wrong_values:
            self.assertEqual(parser.new_account_check(i), False)

    def test_new_account_check_for_correct_values(self):
        '''test that output will be dict and correct'''
        parser = Parsers()
        obj = parser.new_account_check("new_account name=alexey \
        cash=1 debit=2 credit=3 savings=4")

        self.assertEqual(obj['cash'], '1')
        self.assertEqual(obj['debit'], '2')
        self.assertEqual(obj['credit'], '3')
        self.assertEqual(obj['savings'], '4')
        self.assertEqual(isinstance(obj, dict), True)

    def test_open_account_check_for_wrong_values(self):
        '''test wrong names for accout to be opened will be filtered'''
        parser = Parsers()
        for i in open_account_wrong_values:
            self.assertEqual(parser.open_account_check(i), False)

    def test_open_account_check_for_correct_values(self):
        '''test correct name will be returned'''
        parser = Parsers()
        obj = parser.open_account_check("open_account name=test")
        self.assertEqual(obj, 'test')
        self.assertEqual(isinstance(obj, str), True)

    def test_history_check_for_wrong_values(self):
        '''test wrong history requests will be filtered'''
        parser = Parsers()
        for i in history_wrong_values:
            self.assertEqual(parser.history_check(i), False)

    def test_history_check_for_correct_values(self):
        '''test return will be correct and str'''
        parser = Parsers()
        obj = parser.history_check("history records=10")
        self.assertEqual(obj, '10')
        self.assertEqual(isinstance(obj, str), True)

    def test_payments_check_for_wrong_values(self):
        '''test wrong inputs will be filtered'''
        parser = Parsers()
        for i in payments_wrong_values:
            self.assertEqual(parser.payments_check(i), False)

    def test_payments_check_for_correct_values(self):
        '''test correct values will be returned as str'''
        parser = Parsers()
        obj = parser.payments_check("payments records=10")
        self.assertEqual(obj, '10')
        self.assertEqual(isinstance(obj, str), True)

    def test_income_check_for_wrong_values(self):
        '''test wrong values will be ignored'''
        parser = Parsers()
        for i in income_wrong_values:
            self.assertEqual(parser.income_check(i), False)

    def test_income_check_for_correct_values(self):
        '''test return dict object for correct income'''
        parser = Parsers()
        obj = parser.income_check(
            "income category=cash value=120 comment=test")
        self.assertEqual(obj['category'], 'cash')
        self.assertEqual(obj['value'], '120')
        self.assertEqual(obj['comment'], 'test')
        self.assertEqual(isinstance(obj, dict), True)

    def test_withdraw_check_for_wrong_values(self):
        '''test wrong values will be ignored'''
        parser = Parsers()
        for i in withdraw_wrong_values:
            self.assertEqual(parser.withdraw_check(i), False)

    def test_withdraw_check_for_correct_values(self):
        '''test return dict object for new payment as withdraw'''
        parser = Parsers()
        obj = parser.withdraw_check(
            "withdraw category=credit value=120 comment=test")
        self.assertEqual(obj['category'], 'credit')
        self.assertEqual(obj['value'], '120')
        self.assertEqual(isinstance(obj, dict), True)

    def test_pay_check_for_wrong_values(self):
        '''test wrong values will be ignored'''
        parser = Parsers()
        for i in wrong_pay_values:
            self.assertEqual(parser.pay_check(i), False)

    def test_pay_check_for_correct_values(self):
        '''test we will get correct dict'''
        parser = Parsers()
        obj = parser.pay_check(
            "pay category=cash value=100 comment=test")
        self.assertEqual(obj['category'], 'cash')
        self.assertEqual(obj['value'], '100')
        self.assertEqual(obj['comment'], 'test')
        self.assertEqual(isinstance(obj, dict), True)

    def test_debug_check(self):
        '''test return string of turning on or off the stdout logger'''
        parser = Parsers()
        for i in wrong_debug_values:
            self.assertEqual(parser.debug_check(i), False)

        obj = parser.debug_check("debug on")
        self.assertEqual(obj, "on")
        obj = parser.debug_check("debug off")
        self.assertEqual(obj, "off")

if __name__ == "__main__":
    unittest.main()
