from datetime import datetime


class Account(object):
    '''Base class for all accounts'''

    def __init__(self):
        self.description = 'Base Account Class - not for use!'
        self._last_id = 0
        self._last_updated = ''
        self._value = 0
        self._in_sync = False

    def clear(self):
        self._last_id = 0
        self._value = 0
        self._in_sync = True

    @property
    def last_id(self):
        return self._last_id

    @property
    def last_updated(self):
        return self._last_updated

    @property
    def in_sync(self):
        return self._in_sync

    def synchronize(self):
        self._last_updated = datetime.now().strftime("%Y-%m-%d %H:%M")
        self._last_id += 1
        self._in_sync = True

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self.synchronize()
        return True

    def __repr__(self):
        text = super(Account, self).__repr__()
        return "\"[{0}]\" object: {1}".format(self.description, text)


class Cash(Account):
    '''Just cash account where paper money are stored'''

    def __init__(self):
        super(Cash, self).__init__()
        self.description = 'Cash'


class Credit(Account):
    '''Credit account where credit card balance stored'''

    def __init__(self):
        super(Credit, self).__init__()
        self.description = 'Credit'
        self.rate = 0


class Debit(Account):
    '''Debit account where salary card balance is stored'''

    def __init__(self):
        super(Debit, self).__init__()
        self.description = 'Debit'


class Savings(Account):
    '''Savings account where $ and other savings are stored'''

    def __init__(self):
        super(Savings, self).__init__()
        self.description = 'Savings'
        self.currency = 'RUB'
        self.exchange_rate = 1
