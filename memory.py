from datetime import datetime


class BalanceHistory(object):
    '''This is imutable memory unit, containing balance history'''

    def __init__(self):
        self.balance_records = []

    def put_record(self, record):
        if isinstance(record, BalanceRecord):
            self.balance_records.append(record)
            return True
        else:
            return False

    def get_record(self, records_range):
        return self.balance_records[:records_range]
# You can select the latest protocol with the -1 argument.
# if we use slots and pickle, we got
# TypeError: a class that defines __slots__ without
# defining __getstate__ cannot be pickled

# BUT
# This is actually incorrect.
# This message comes from the oldest protocol, which is the default.
# In Python 2.7 this would be 2 (which was introduced in 2.3),
# and in 3.6 it is 4.
#        with open('records.pickle', 'wb') as f:
#            pickle.dump(biig, f, -1)

# just perfectly saved and loaded
# list stores array of our needed objects ideally


class BalanceRecord(object):
    '''This is just record ready to be stored in history'''
    __slots__ = ['last_id', 'date', 'cash', 'debit', 'credit', 'savings']

    def __init__(self, cash, debit, credit, savings):
        self.last_id = 0
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.cash = cash
        self.debit = debit
        self.credit = credit
        self.savings = savings


class PayHistory(object):
    '''This is imutable memory unit, containing all money records'''

    def __init__(self):
        # question here is:
        # if we save to pickle and then load
        # will the list be empty?
        self.pay_records = []

        # oh wait, we will assign here values from our file

    # we generate payment object in cmd mux
    # then we send it to payhistory object
    # who loads everything
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
        # TODO: need to think about out of range error!


class PayRecord(object):
    '''Class ready to be stored in history of Payments Incomes'''
    __slots__ = ['last_id', 'date', 'category', 'value', 'comment']

    def __init__(self, category, value, comment):
        self.last_id = 0
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.category = category
        self.value = value
        self.comment = comment
