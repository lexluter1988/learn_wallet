import cPickle as pickle
from datetime import datetime


class BalanceHistory(object):
    '''This is imutable memory unit, containing balance history'''

    def __init__(self):
        pass

    def save_a_lot(self):
        biig = []
        for i in range(1000000):
            itemm = BalanceRecord(i)
            biig.append(itemm)

# You can select the latest protocol with the -1 argument.
# if we use slots and pickle, we got
# TypeError: a class that defines __slots__ without
# defining __getstate__ cannot be pickled

# BUT
# This is actually incorrect.
# This message comes from the oldest protocol, which is the default.
# In Python 2.7 this would be 2 (which was introduced in 2.3),
# and in 3.6 it is 4.
        with open('records.pickle', 'wb') as f:
            pickle.dump(biig, f, -1)

# just perfectly saved and loaded
# list stores array of our needed objects ideally


class BalanceRecord(object):
    '''This is just record ready to be stored in history'''
    __slots__ = ['id', 'date', 'cash', 'debit', 'credit', 'savings']

    def __init__(self):
        self.id = 0
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.cash = 0
        self.debit = 0
        self.credit = 0
        self.savings = 0


class PayHistory(object):
    '''This is imutable memory unit, containing all money records'''

    def __init__(self):
        pass


class PayRecord(object):
    '''Class ready to be stored in history of Payments Incomes'''
    __slots__ = ['id', 'date', 'category', 'value']

    def __init__(self):
        self.id = 0
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.category = 0
        self.value = 0
