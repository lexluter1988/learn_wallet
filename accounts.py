# import cPickle as pickle
from datetime import datetime


class Account(object):
    '''Base class for all accounts'''

    def __init__(self, clean=False):
        self.clean = clean
        self.description = 'Base Account Class - not for use!'
        self.__last_id = 0
        self.__last_updated = ''
        self.__value = 0
        self.__in_sync = False

    def clear(self):
        if self.clean:
            self.__last_id = 0
            self.__value = 0
            self.__in_sync = True

    @property
    def last_id(self):
        return self.__last_id

    @property
    def last_updated(self):
        return self.__last_updated

    @property
    def in_sync(self):
        return self.__in_sync

    def synchronize(self):
        self.__last_updated = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.__last_id += 1
        self.__in_sync = True

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value += value
        self.synchronize()
        return True

    # def get_balance(self):
    #     # need try cause we have EOFError exception
    #     try:
    #         f = None
    #         f = open('account.pickle', 'rb')
    #         self.temp = pickle.load(f)

    #     except IOError:
    #         pass
    #     except EOFError:
    #         pass

    #     finally:
    #         if f:
    #             f.close()

    def __repr__(self):
        text = super(Account, self).__repr__()
        return "\"[{0}]\" object: {1}".format(self.description, text)


class Cash(Account):
    '''Just cash account where paper money are stored'''

    def __init__(self, clean=False):
        self.description = 'Cash Account'


class Credit(Account):
    '''Credit account where credit card balance stored'''

    def __init__(self, clean=False):
        self.description = 'Credit Account'
        self.rate = 0


class Debit(Account):
    '''Debit account where salary card balance is stored'''

    def __init__(self, clean=False):
        self.description = 'Debit Account'


class Savings(Account):
    '''Savings account where $ and other savings are stored'''

    def __init__(self, clean=False):
        self.description = 'Savings Account'
        self.currency = 'RUB'
