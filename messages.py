class Messages(object):

    hello_message = '''
    Welcome to \'Fucking Wallet\'!
    '''

    quit_message = '''
    Goodbye Fella!
    '''

    help_message = '''
    [basics]
        'help' - to get cmd list
        'tutorial' - to get full description
        'quit' - just quit program

    [operations]
        'init' - initiate wallet
        'income <cash|debit|credit|savings> <sum>' - put money
        'pay <cash|debit|credit|savings> <sum>' - spend money
        'withdraw <debit|credit|savings> <amount>' - from any account into cash

    [stats]
        'balance' - show current stats of your wallet
        'cash'- how much cash you have
        'debit' - how much on salary account
        'credit' - how much you own
        'savings' - how much you save for your future

    [history]
        'history <last records>, default=5>' - show last balance changes
        'payments <last records>, default=5>' - show last payments
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

    balance_message = '''
    Here is your balance
    '''
