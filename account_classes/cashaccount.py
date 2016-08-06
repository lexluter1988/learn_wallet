from account import Account


class CashAccount(Account):
    '''Just cash account where paper money are stored'''

    def __init__(self, value=0, clean=False):
        self.description = 'Cash Account'
        self.last_updated = ''
        self.value = 0
        self.in_sync = False
