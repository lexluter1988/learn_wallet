class Messages(object):

    hello_message = '''
    Welcome to \'Fucking Wallet\'!
    '''

    help_message = '''
    'help' - to get cmd list
    'tutorial' - to get full description
    'init <cash|debit|credit|savings|>' - initiate wallet
    'balance' - show current stats of your wallet
    'cash'- how much cash you have
    'debit' - how much on salary account
    'credit' - how much on credit
    'history <last records>, default=5>' - show last balance changes
    'payments <last records>, default=5>' - show last payments
    'withdraw <amount>' - take money from credit or debit account into cash
    'pay <cash|debit|credit|savings|> <sum> <comment>' - spend money
    'earn <cash|debit|credit|savings|> <sum> <comment>' - put money
    'quit' - just quit program
    '''

    tutorial_message = '''
    Welcome to the tutorial!

    Start by initiating your wallet \'init\', set values
    List your current stats for all stores (balance)
    Or list specific store (cash|debit|credit|savings)
    See your history (history) for last days

    See how you spend your money (payments)
    Pay for something (pay) or withdraw your cash
    When payday come - put (earn) something in any of your account
    Good luck!
    '''
