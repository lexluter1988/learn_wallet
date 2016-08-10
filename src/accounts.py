from datetime import datetime
from exceptions import NotMoneyError


class Account(object):
    '''Base class for all accounts'''

    def __init__(self):
        self.description = 'Base Account Class - not for use!'
        self._last_id = 0
        self._last_updated = ''
        self._value = 0
        self._in_sync = False

    def clear(self):
        '''for future features, not used anywhere now'''
        self._last_id = 0
        self._value = 0
        self._in_sync = True

    @property
    def last_id(self):
        '''for future features, not used anywhere now'''
        return self._last_id

    @property
    def last_updated(self):
        '''for future features, not used anywhere now'''
        return self._last_updated

    @property
    def in_sync(self):
        '''for future features, not used anywhere now'''
        return self._in_sync

    def synchronize(self):
        '''for future features, not used anywhere now'''
        self._last_updated = datetime.now().strftime("%Y-%m-%d %H:%M")
        self._last_id += 1
        self._in_sync = True

    @property
    def value(self):
        '''primary weak property to set values for accounts'''
        return self._value

    @value.setter
    def value(self, value):
        '''primary setter for weak property'''
        if not isinstance(value, int):
            raise NotMoneyError
        self._value = value
        self.synchronize()
        return True

    def __repr__(self):
        '''representation for class name'''
        text = super(Account, self).__repr__()
        return "\"[{0}]\" object: {1}".format(self.description, text)


class Cash(Account):
    '''Cash account where paper money are stored'''

    def __init__(self):
        super(Cash, self).__init__()
        self.description = 'Cash'


class Credit(Account):
    '''Credit account where credit card balance stored, always negative'''

    # for credit it is important to know
    # if this is first init of credit
    # or if we update it
    def __init__(self, clean=False):
        super(Credit, self).__init__()
        self.description = 'Credit'
        self.clean = clean
        # rate is for future
        # to calculate %

        # TODO: include credit limit
        self.rate = 0

    @property
    def value(self):
        return self._value

    # rewriten property cause credit is always negative
    @value.setter
    def value(self, value):
        if not isinstance(value, int):
            raise NotMoneyError
        # so, we always initiate credit as negative value
        # cause regexp for new_account will not take
        # negative input for credit, therefore we always have correct
        # input value
        if self.clean:
            self._value -= value
            # and we should of course switch account
            # to not clean after that
            self.clean = False
        else:
            # as soon as credit will be initiated
            # we work with it as usual
            # if you take money - we subtract
            # if you put money - we add
            # like any other account
            self._value = value
        self.synchronize()
        return True


class Debit(Account):
    '''Debit account where salary card balance is stored'''

    def __init__(self):
        super(Debit, self).__init__()
        self.description = 'Debit'


class Savings(Account):
    '''Savings account where $ or RUB and other savings are stored'''

    def __init__(self):
        super(Savings, self).__init__()
        self.description = 'Savings'
        # for future features
        # http://openexchangerates.readthedocs.io/en/latest/content/configure.html
        # to get up-to-date $ rate, in case we have dollars
        # TODO: include ability to have few different accounts
        self.currency = 'RUB'
        self.exchange_rate = 1
