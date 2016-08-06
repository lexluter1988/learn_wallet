from account import Account


class DebitAccount(Account):
    '''Debit account where salary card balance is stored'''

    def __init__(self, value=0, clean=False):
        self.description = 'Debit Account'
        self.last_updated = ''
        self.value = 0
        self.in_sync = False
