import re


class Parsers(object):
    '''list of patterns and functions to parse any allowed input'''

    # logger switch pattern
    # we call it like
    # debug on
    # debug off
    logger_check_pattern = r"" \
                           r"(\s)*(debug)(\s){1,1}(?P<switch>\w{1,3})" \
                           r"(\s)*"

    # parses new_account command to match
    # 'new_account'
    #        name= <string>
    #        cash= <int>
    #        debit= <int>
    #        credit= <int>
    #        savings= <int>
    new_account_pattern = r"" \
                          r"(\s)*(?P<cmd>new_account)" \
                          r"(\s)+(name=)(?P<name>\w{1,10})" \
                          r"(\s)+(cash=)(?P<cash>\d{1,10})" \
                          r"(\s)+(debit=)(?P<debit>\d{1,10})" \
                          r"(\s)+(credit=)(?P<credit>\d{1,10})" \
                          r"(\s)+(savings=)(?P<savings>\d{1,10})" \
                          r"(\s)*"

    # parses open_account command to match
    # 'open_account' name= <string>
    open_account_pattern = r"" \
                           r"(\s)*(?P<cmd>open_account)" \
                           r"(\s)+(name=)(?P<name>\w{1,10})" \
                           r"(\s)*"

    # parses history command to match
    # 'history' records= <int>
    history_pattern = r"" \
                      r"(\s)*(?P<cmd>history)" \
                      r"(\s)+(records=)(?P<records>\d{1,5})"\
                      r"(\s)*"

    # parses payments command to match
    # 'payments' records= <int>
    payments_pattern = r"" \
                       r"(\s)*(?P<cmd>payments)" \
                       r"(\s)+(records=)(?P<records>\d{1,5})" \
                       r"(\s)*"

    # parses income command  to match
    # 'income'
    #    value= <string>
    #    category= <string>
    #    comment= <string>
    # TODO:
    # >>> pars.income_check('income value=1000 category=cash comment=fuck you')
    # {'category': 'cash', 'comment': 'fuck', 'value': '1000'}

    income_pattern = r"" \
                     r"(\s)*(?P<cmd>income)" \
                     r"(\s)+(category=)(?P<category>\w{1,10})" \
                     r"(\s)+(value=)(?P<value>\d{1,10})" \
                     r"(\s)+(comment=)(?P<comment>\w{1,50})" \
                     r"(\s)*"

    # parses withdraw command to match
    # 'withdraw'
    #    category= <string>
    #    value= <int>
    withdraw_pattern = r"" \
                       r"(\s)*(?P<cmd>withdraw)" \
                       r"(\s)+(category=)(?P<category>\w{1,10})" \
                       r"(\s)+(value=)(?P<value>\d{1,10})" \
                       r"(\s)*"

    # parses pay command to match
    # 'pay'
    #    category= <string>
    #    value= <int>
    #    comment= <string>

    # we can have that if doublicat group names
    # raise error, v # invalid expression
    # sre_constants.error: redefinition of group name 'value' as group 11

    pay_pattern = r"" \
                  r"(\s)*(?P<cmd>pay)" \
                  r"(\s)+(category=)(?P<category>\w{1,10})" \
                  r"(\s)+(value=)(?P<value>\d{1,10})" \
                  r"(\s)+(comment=)(?P<comment>\w{1,10})" \
                  r"(\s)*"

    def __init__(self):
        pass

    def new_account_check(self, cmd):
        '''return dict object for new account'''
        check = re.match(self.new_account_pattern, str(cmd))
        if check:
            blueprint = {'name': check.group('name'),
                         'cash': check.group('cash'),
                         'debit': check.group('debit'),
                         'credit': check.group('credit'),
                         'savings': check.group('savings')}
            return blueprint
        else:
            return False

    def open_account_check(self, cmd):
        '''return string name for accout to be opened'''
        check = re.match(self.open_account_pattern, str(cmd))
        if check:
            return check.group('name')
        else:
            return False

    def history_check(self, cmd):
        '''return int num of records to get from history of balance'''
        check = re.match(self.history_pattern, str(cmd))
        if check:
            return check.group('records')
        else:
            return False

    def payments_check(self, cmd):
        '''return int num of payments to get from payments history'''
        check = re.match(self.payments_pattern, str(cmd))
        if check:
            return check.group('records')
        else:
            return False

    def income_check(self, cmd):
        '''return dict object for new payment as income'''
        check = re.match(self.income_pattern, str(cmd))
        if check:
            blueprint = {'category': check.group('category'),
                         'value': check.group('value'),
                         'comment': check.group('comment')}
            return blueprint
        else:
            return False

    def withdraw_check(self, cmd):
        '''return dict object for new payment as withdraw'''
        check = re.match(self.withdraw_pattern, str(cmd))
        if check:
            blueprint = {'category': check.group('category'),
                         'value': check.group('value')}
            return blueprint
        else:
            return False

    def pay_check(self, cmd):
        '''return dict object for new payment as pay for some goods'''
        # i'm setting str convertation for NoneType fix
        check = re.match(self.pay_pattern, str(cmd))
        if check:
            blueprint = {'category': check.group('category'),
                         'value': check.group('value'),
                         'comment': check.group('comment')}
            return blueprint
        else:
            return False

    def debug_check(self, cmd):
        '''return string of turning on or off the stdout logger'''
        check = re.match(self.logger_check_pattern, str(cmd))
        if check:
            return check.group('switch')
        else:
            return False
