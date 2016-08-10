from datetime import datetime


class BalanceHistory(object):
    '''This is imutable memory unit, containing balance history'''

    def __init__(self):
        # we store it as list
        # empty at first, then it will always loaded from pickle file
        self.balance_records = []

    def put_record(self, record):
        '''like any list, we just append records'''
        if isinstance(record, BalanceRecord):
            self.balance_records.append(record)
            return True
        else:
            return False

    def get_record(self, records_range):
        '''good thing about list, that dispite of range
        we do not have problems if range > len(list)'''
        return self.balance_records[:records_range]
# You can select the latest protocol with the -1 argument.
# if we use slots and pickle, we got
# TypeError: a class that defines __slots__ without
# defining __getstate__ cannot be pickled

# BUT: this is actually incorrect.
# This message comes from the oldest protocol, which is the default.
# In Python 2.7 this would be 2 (which was introduced in 2.3),
# and in 3.6 it is 4.
#        with open('records.pickle', 'wb') as f:
#            pickle.dump(biig, f, -1)

# just perfectly saved and loaded
# list stores array of our needed objects ideally


class BalanceRecord(object):
    '''This is record ready to be stored in history'''
    __slots__ = ['last_id', 'date', 'cash', 'debit', 'credit', 'savings']


    def __init__(self, cash, debit, credit, savings):
        self.last_id = 0
        # last date generated automatically
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.cash = cash
        self.debit = debit
        self.credit = credit
        self.savings = savings


class PayHistory(object):
    '''This is imutable memory unit, containing all money records'''

    def __init__(self):
        self.pay_records = []

    def put_payment(self, payment):
        if isinstance(payment, PayRecord):
            self.pay_records.append(payment)
            return True
        else:
            return False

    # getting record is also simple
    # by sending id as how much we want to see
    def get_payment(self, payments_range):
        return self.pay_records[:payments_range]
        # note: this is always list
        # even if 1 object


class PayRecord(object):
    '''PayRecord object ready to be stored in history of Payments/Incomes'''
    __slots__ = ['last_id', 'date', 'category', 'sign', 'value', 'comment']

    def __init__(self, category, value, comment):
        # that is why id for payments don't increase, i should set it by miself
        self.last_id = 0
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.category = category
        self.sign = '+'
        self.value = value
        self.comment = comment
