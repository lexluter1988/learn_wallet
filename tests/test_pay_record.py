import unittest
from datetime import datetime
from ..src.memory import PayRecord


class CheckPayRecord(unittest.TestCase):

    def test_creation(self):
        '''just check for type of object created and values'''
        pay = PayRecord('cash', 100, 'comment')
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.assertEqual(pay.last_id, 0)
        self.assertEqual(pay.date, current_time)
        self.assertEqual(pay.category, 'cash')
        self.assertEqual(pay.value, 100)
        self.assertEqual(pay.comment, 'comment')
        self.assertEqual(isinstance(pay, PayRecord), True)
