import unittest
from datetime import datetime
from ..src.memory import BalanceRecord


class CheckBalanceRecord(unittest.TestCase):

    def test_creation(self):
        '''just check for type of object created and values'''
        balance = BalanceRecord(1, 2, 3, 4)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.assertEqual(balance.last_id, 0)
        self.assertEqual(balance.date, current_time)
        self.assertEqual(balance.cash, 1)
        self.assertEqual(balance.debit, 2)
        self.assertEqual(balance.credit, 3)
        self.assertEqual(balance.savings, 4)
        self.assertEqual(isinstance(balance, BalanceRecord), True)
