class Messages(object):

    hello_message = '''
    Welcome to \'Fucking Wallet\'!
    '''

    quit_message = '''
    Goodbye Fella!
    '''

    help_message = '''
    [basics]
        'open_account name=<account name>' - open your account
        'new_account name=<account name>
                cash=<value>
                debit=<value>
                credit=<value>
                savings=<value>' - create new account with all settings

        'help' - to get cmd list
        'tutorial' - to get full description
        'quit' - just quit program

    [operations]
        'income
            category=<cash|debit|credit|savings>
            value=<sum>' - put money
        'pay
            category=<cash|debit|credit|savings>
            value=<sum>
            comment=<comment>' - spend money
        'withdraw
            category=<debit|credit|savings>
            value=<amount>' - from any account into cash

    [stats]
        'balance' - show current stats of your wallet
        'cash'- how much cash you have
        'debit' - how much on salary account
        'credit' - how much you own
        'savings' - how much you save for your future

    [history]
        'history records=<last records>' - show last balance changes
        'payments records<last records>' - show last payments
    '''

    tutorial_message = '''
    Welcome to the tutorial!

    Start using your wallet, create new one (new_account)
    Or continue using your old file (open_account)
    List your current stats for all stores (balance)
    Or list specific store (cash|debit|credit|savings)
    See your history (history) for last days

    See how you spend your money (payments)
    Pay for something (pay) or withdraw your cash
    When payday come - put (income) something in any of your account
    Good luck!
    '''

    no_account_message = '''
    You haven't opened any account

    Please initiate new one(new_account)
    Or open existing (open_account)

    You can also see 'help' page and 'tutorial'
    '''

    new_account_message = '''Account for you created'''
    open_account_message = '''Your account loaded'''
    balance_message = '''Balance'''
    cash_message = '''Cash'''
    debit_message = '''Ddebit'''
    credit_message = '''Credit'''
    savings_message = '''Savings'''
    history_message = '''Here is last balance histoty'''
    payments_message = '''Last payments'''
    pay_message = '''You payed for something'''
    income_message = '''We got money'''
    withdraw_message = '''Taking money from account to cash'''
    succes_withdraw_message = '''Succesfully took money into cash'''
    save_message = '''Data saved'''
    snapshot_history_message = '''Balance History updated'''

# errors
    basic_input_error = '''You entered incorrect values'''
    pay_category_error = '''No such category for payments'''
    pay_no_money_error = '''You do not have so much money on that category'''
    income_category_error = '''No such category for incomes'''
    withdraw_category_error = '''You cannot take money from cash to cash'''
    history_error = '''Invalid history request'''
