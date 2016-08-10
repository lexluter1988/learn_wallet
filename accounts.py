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

    # for credit it is important to know
    # if this is first init of credit
    # or if we update it
    def __init__(self, clean=False):
        super(Credit, self).__init__()
        self.description = 'Credit'
        self.clean = clean
        # rate is for future
        # to calculate %
        self.rate = 0

    @property
    def value(self):
        return self._value

    # rewriten property cause credit is always negative
    @value.setter
    def value(self, value):
        # so, we always initiate credit as negative value
        # since regexp for new_account cannot take
        # negative input for credit -> we always have correct
        # value
        if self.clean:
            self._value -= value
            # and we should of course switch account
            # to not clean after that
            self.clean = False
        else:
            # as soon as credit already initiated
            # we work with it as usual
            # if you take money - we subtract
            # if you put money - we add
            self._value = value
        self.synchronize()
        return True


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
        # for future features
        # http://openexchangerates.readthedocs.io/en/latest/content/configure.html
        # to get up-to-date $ rate, in case safe in dollars
        self.currency = 'RUB'
        self.exchange_rate = 1
