from account import Account


class SavingsAccount(Account):
    '''Savings account where $ and other savings are stored'''

    def __init__(self, value=0, clean=False):
        self.description = 'Savings Account'
        self.last_updated = ''
        self.value = 0
        self.currency = 'RUB'
        self.in_sync = False
