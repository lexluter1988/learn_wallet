class Messages(object):

    hello_message = '''
    Welcome to \'Fucking Wallet\'!
    '''

    quit_message = '''
    Goodbye Fella!
    '''

    help_message = '''
    [logger]
    debug on, debug off

    [basics]
    'help', 'tutorial, 'open_account', 'new_account', 'quit'

    [operations]
    'income', 'pay', 'withdraw'

    [stats]
    'balance', 'cash', 'debit', 'credit', 'savings'

    [history]
    'history', 'payments'
    '''

    tutorial_message = '''
    Welcome to the tutorial!

    Start by creating new wallet. (new_account)
    Specify all cash,debit,credit,savings values.

    Or continue using your old wallet. (open_account)
    List your current stats for all stores. (balance)

    Or list specific store. (cash|debit|credit|savings)
    See your history (history) for last days, how balance changed.

    See how you spend your money (payments) for last days.
    Pay for something (pay) or withdraw from account into cash.
    When payday come - put (income) something in any of your account.
    Good luck!
    '''

    no_account_message = '''
    No accounts opened. Use 'new_account' or 'open_account'
    Also see 'help' page and 'tutorial' if you questions.
    '''

    new_account_message = '''account created'''
    open_account_message = '''account loaded'''
    balance_message = '''balance'''
    cash_message = '''cash'''
    debit_message = '''debit'''
    credit_message = '''credit'''
    savings_message = '''savings'''
    history_message = '''last balance changes history'''
    payments_message = '''your last payments'''
    pay_message = '''payment recieved'''
    income_message = '''great, we got money'''
    withdraw_message = '''taking money from accounts to cash'''
    succes_withdraw_message = '''succesfull withdraw'''
    save_message = '''data saved'''
    snapshot_history_message = '''balance history updated'''
    logger_off = '''debug log turned off'''
    logger_on = '''debug log turned on'''

# errors
    basic_input_error = '''you entered incorrect values'''
    new_account_error = '''incorrect values for new account'''
    open_account_error = '''unable to open account'''
    open_account_name_error = '''unable to open, incorrect arguments'''
    no_exists_error = '''account with that name does not exist'''
    pay_category_error = '''wrong category, use [cash,debit,credit,savings]'''
    pay_error = '''unable to proceed payment, invalid arguments'''
    pay_no_money_error = '''you do not have so much money in this account'''
    income_error = '''unable to put income, invalid arguments'''
    income_category_error = '''no such category for incomes'''
    withdraw_category_error = '''you cannot take money from cash to cash'''
    withdraw_error = '''unable to proceed withdraw, invalid arguments'''
    history_error = '''invalid history request, specify <records=>'''
    payments_error = '''invalid payments request, specify <records=>'''
    logger_error_on = '''debug log already turned on'''
    logger_error_off = '''debug log already turned off'''
    logger_error = '''invalid parameters for logger'''
