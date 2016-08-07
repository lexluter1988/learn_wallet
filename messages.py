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

    Start using your wallet, it's already initiated
    List your current stats for all stores (balance)
    Or list specific store (cash|debit|credit|savings)
    See your history (history) for last days

    See how you spend your money (payments)
    Pay for something (pay) or withdraw your cash
    When payday come - put (income) something in any of your account
    Good luck!
    '''

    no_account_message = '''
    You haven't opened any account.
    Please initiate new one(new_account)
    Or open existing (new_account)
    '''

    new_account_message = '''Account for you created'''
    open_account_message = '''Your account loaded'''
    balance_message = '''Your balance'''
    cash_message = '''Your cash'''
    debit_message = '''Your debit'''
    credit_message = '''Your credit'''
    savings_message = '''Your savings'''
    history_message = '''Here is last balance histoty'''
    payments_message = '''Last payments'''
    pay_message = '''You payed for something'''
    income_message = '''We got money'''
    withdraw_message = '''Taking money from account to cash'''
    save_message = '''Data saved'''
