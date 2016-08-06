import cPickle as pickle


class BalanceHistory(object):
    '''This is imutable memory unit, containing balance history'''

    def __init__(self):
        pass

    def save_a_lot(self):
        biig = []
        for i in range(1000000):
            itemm = BalanceRecord(i)
            biig.append(itemm)

        with open('records.pickle', 'wb') as f:
            pickle.dump(biig, f, -1)

# just perfectly saved and loaded
# list stores array of our needed objects ideally


class BalanceRecord(object):
    '''This is just record ready to be stored in history'''
    __slots__ = ['id', 'date', 'category', 'amount', 'comment']

# if we use slots and pickle, we got
# TypeError: a class that defines __slots__ without
# defining __getstate__ cannot be pickled

# BUT
# This is actually incorrect.
# This message comes from the oldest protocol, which is the default.
# You can select the latest protocol with the -1 argument.
# In Python 2.7 this would be 2 (which was introduced in 2.3),
# and in 3.6 it is 4.

    def __init__(self, amount=0, category='cash', *args):
        self.id = 0
        self.date = '2016-08-03'
        self.category = category
        self.amount = amount
        self.comment = args


class PayHistory(object):
    '''This is imutable memory unit, containing all money records'''

    def __init__(self):
        pass


# actually really shitty name for class
# too fucking long


class PayRecord(object):
    '''Class ready to be stored in history of Payments Incomes'''

    def __init__(self):
        pass
