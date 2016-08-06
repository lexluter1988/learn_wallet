from account import Account


class CreditAccount(Account):
    '''Credit account where credit card balance stored'''

    def __init__(self, value=0, clean=False):
        self.description = 'Credit Account'
        self.last_updated = ''
        self.value = 0
        self.interest_rate = 0
        self.in_sync = False
