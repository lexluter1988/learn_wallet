import cPickle as pickle


class Account(object):
    '''Base class for all accounts'''

    def __init__(self, value=0, clean=False):
        self.description = 'Base Account'
        self.last_updated = ''
        self.value = value
        self.in_sync = False

    def get_balance(self):
        # need try cause we have EOFError exception
        try:
            f = None
            f = open('account.pickle', 'rb')
            self.temp = pickle.load(f)

        except IOError:
            pass
        except EOFError:
            pass

        finally:
            if f:
                f.close()

    def set_balance(self):
        pass

    def update_balance(self):
        pass

    def save_data(self):
        with open('account.pickle', 'wb') as f:
            pickle.dump(self, f)

    def load_data(self):
        pass

    def __repr__(self):
        text = super(Account, self).__repr__()
        return "\"[{0}]\" object: {1}".format(self.description, text)


class Cash(Account):
    '''Just cash account where paper money are stored'''

    def __init__(self, value=0, clean=False):
        self.description = 'Cash Account'
        self.last_updated = ''
        self.value = 0
        self.in_sync = False


class Credit(Account):
    '''Credit account where credit card balance stored'''

    def __init__(self, value=0, clean=False):
        self.description = 'Credit Account'
        self.last_updated = ''
        self.value = 0
        self.interest_rate = 0
        self.in_sync = False


class Debit(Account):
    '''Debit account where salary card balance is stored'''

    def __init__(self, value=0, clean=False):
        self.description = 'Debit Account'
        self.last_updated = ''
        self.value = 0
        self.in_sync = False


class Savings(Account):
    '''Savings account where $ and other savings are stored'''

    def __init__(self, value=0, clean=False):
        self.description = 'Savings Account'
        self.last_updated = ''
        self.value = 0
        self.currency = 'RUB'
        self.in_sync = False



