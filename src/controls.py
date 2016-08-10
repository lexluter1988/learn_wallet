import logging
import sys
import time
import random
import cPickle as pickle
from utils import Parsers
from messages import Messages as msg
from accounts import Cash, Debit, Credit, Savings
from memory import BalanceHistory, PayHistory
from memory import BalanceRecord, PayRecord

# tuple of commands we can call with no arguments
# commands like getters of values
# no arguments needed here
static_commands = ('hello',
                   'help',
                   'tutorial',
                   'save',
                   'quit',
                   'cash',
                   'balance',
                   'debit',
                   'credit',
                   'no_account',
                   'savings',)

# allowed category tuple
category_list = ('cash',
                 'debit',
                 'credit',
                 'savings', )


# allowed accounts for withdraw
withdraw_category_list = ('debit',
                          'credit',
                          'savings',)


class CmdLog(type):
    '''Commands logger metaclass, used only for commands'''

    def __new__(cls, name, bases, namespace, **kwargs):
        # basic metaclass override of new method
        result = type.__new__(cls, name, bases, dict(namespace))

        # logger to file
        result.file_handler = logging.FileHandler('wallet.log')
        result.file_handler.setFormatter(logging.Formatter(
            '%(asctime)s [%(levelname)s] [%(name)s] - %(message)s'))
        result.file_handler.setLevel(logging.DEBUG)

        # logger to stdout
        result.out_handler = logging.StreamHandler(sys.stdout)
        # format logger to write in stdout
        # we write in format like:
        # '1970-01-10, 15:49:12,913 [INFO] [CheckMeta] - Hello World!'
        result.out_handler.setFormatter(logging.Formatter(
            '%(asctime)s [%(levelname)s] [%(name)s] - %(message)s'))
        result.out_handler.setLevel(logging.DEBUG)

        # adjust our metaclass to contain logger from beginning
        result.logger = logging.getLogger(name)
        result.logger.addHandler(result.out_handler)
        result.logger.addHandler(result.file_handler)
        result.logger.setLevel(logging.DEBUG)

        return result


class CmdMux(object):
    '''This is the main control unit, sends command to all units'''
    # use our logger metaclass
    __metaclass__ = CmdLog

    def __init__(self):
        # class like singleton
        # we have all parsers here
        # all records blueprints
        # last record id as well here
        self.console_logger = True
        self.prs = Parsers()
        self.account_opened = False
        self.record_id = 0
        self.logger.debug("Created multiplexer for user's commands")

    # switcher for loggers
    def debug(self, params):
        debug_toggle = self.prs.debug_check(params)
        if debug_toggle:
            if self.console_logger and debug_toggle == 'on':
                return msg.logger_error_on
            elif self.console_logger and debug_toggle == 'off':
                self.console_logger = False
                self.logger.removeHandler(self.out_handler)
                return msg.logger_off
            elif not self.console_logger and debug_toggle == 'off':
                return msg.logger_error_off
            else:
                self.console_logger = True
                self.logger.addHandler(self.out_handler)
                return msg.logger_on
        else:
            return msg.logger_error

    # info methods that do not need any value or calculation
    def hello(self):
        self.logger.debug("Wallet program initiated")
        return msg.hello_message

    def quit(self):
        self.logger.debug("Exiting from wallet")
        return msg.quit_message

    def help(self):
        self.logger.debug("Asking for help")
        return msg.help_message

    def tutorial(self):
        self.logger.debug("Asking for tutorial")
        return msg.tutorial_message

    def no_account(self):
        self.logger.error("No accounts opened")
        return msg.no_account_message

    # main work with accounts creation/initialization
    def new_account(self, params):
        '''method that parses already have dict object for new account
        it should create all memory units, records stores, save them
        and write first history records for new account'''
        last_record_id = 0
        self.logger.debug("Creating new clean account")
        # shortest way for now
        # since all store(cash, debit, credit, savings) are
        # secure, I do not assgin values on instance creation
        # only by setters

        # if not all(i is not None and isinstance(i, str) for i in
        # [name, cash, debit, credit, savings]):
        # cannot check cause
        # UnboundLocalError: local variable 'cash' referenced before assignment
        blueprint = self.prs.new_account_check(params)
        if blueprint:
            self.account_opened = True
            # creating temp objects
            tmpname = blueprint['name']

            # true for credit means it will be
            # initiate like if we already own money
            # of course you can set value 0
            tmpcash, tmpdebit, tmpcredit, tmpsavings = \
                Cash(), Debit(), Credit(True), Savings()

            tmppayments, tmphistory = PayHistory(), BalanceHistory()

            # assigning values
            tmpcash.value = int(blueprint['cash'])
            tmpdebit.value = int(blueprint['debit'])
            tmpcredit.value = int(blueprint['credit'])
            tmpsavings.value = int(blueprint['savings'])

            # saving complete object (new account, everything is empty)
            self.account = {
                'name': tmpname,
                'cash': tmpcash,
                'debit': tmpdebit,
                'credit': tmpcredit,
                'savings': tmpsavings,
                'payments': tmppayments,
                'history': tmphistory,
                'last_record_id': last_record_id,
            }
            self.__snapshot_history()
            # in fact, this is first record of
            # account's life
            self.__save()
            return msg.new_account_message
        else:
            # if we here, blueprint is not correct
            # we send new_account_error
            return msg.new_account_error

    def open_account(self, params):
        '''method to open pickle file, and load just one
        big dict object with all our Cash(), BalanceRecords(), etc'''
        self.logger.debug("Opening your account")
        account_name = self.prs.open_account_check(params)
        if account_name:
            try:
                with open(account_name + '.pickle', 'rb') as f:
                    # in fact we load everything quite easy
                    # into dict object so all methods can work with it
                    self.account = pickle.load(f)
                    # last_record_id is stored in account itself
                    self.record_id = self.account['last_record_id']
                    self.account_opened = True
                    return msg.open_account_message
            except TypeError:
                self.logger.error("Failure during opening")
                return msg.open_account_error
            except IOError:
                self.logger.error("Account does not exist")
                return msg.no_exists_error
        else:
            self.account_opened = False
            return msg.open_account_name_error

    # status methdos, that needs objects of accounts and record
    def balance(self):
        self.logger.debug("Getting current balance")
        account_name = self.account['name']
        out = [self.cash(), self.debit(), self.credit(), self.savings()]
        return "{0} of {1} account\n {2}".format(msg.balance_message,
                                                 account_name, out)

    def cash(self):
        self.logger.debug("Getting your cash")
        account_cash = self.account['cash'].value
        return "{0}: {1}".format(msg.cash_message, account_cash)

    def debit(self):
        self.logger.debug("Getting your debit account")
        account_debit = self.account['debit'].value
        return "{0}: {1}".format(msg.debit_message, account_debit)

    def credit(self):
        self.logger.debug("Getting your credit account")
        account_credit = self.account['credit'].value
        return "{0}: {1}".format(msg.credit_message, account_credit)

    def savings(self):
        self.logger.debug("Getting your savings")
        account_savings = self.account['savings'].value
        return "{0}: {1}".format(msg.savings_message, account_savings)

    # history methods, for last payments and balance history
    def history(self, params):
        self.logger.debug("Getting your last balance history")
        num = self.prs.history_check(params)
        if num:
            # return list of balance record objects
            records = self.account['history'].get_record(int(num))
            # each record is BalanceRecord
            out = ''
            for record in records:
                line = "|{}|{}|cash:{}|debit:{}|credit:{}|safe:{}|\n".format(
                           record.last_id,
                           record.date, record.cash,
                           record.debit, record.credit,
                           record.savings,)
                out += line
            return msg.history_message+'\n'+out
        else:
            return msg.history_error

    def payments(self, params):
        self.logger.debug("Getting you last payments")
        num = self.prs.payments_check(params)
        if num:
            # return list of payments objects
            records = self.account['payments'].get_payment(int(num))
            # each record is PayRecord
            out = ''
            for record in records:
                line = "|{}|{}|from:{}|sum:{}{}|comment:{}|\n".format(
                           record.last_id,
                           record.date, record.category,
                           record.sign, record.value, record.comment,)
                out += line
            return msg.payments_message+'\n'+out
        else:
            return msg.payments_error
        return msg.payments_message

    # real operation methods
    def pay(self, params):
        self.logger.debug("Spending money")
        blueprint = self.prs.pay_check(params)
        if blueprint:
            money_i_have = self.account[blueprint['category']].value
            if blueprint['category'] not in category_list:
                return msg.pay_category_error
            elif ((blueprint['category'] != 'credit') and
                  int(blueprint['value']) > int(money_i_have)):
                return msg.pay_no_money_error
            else:
                pay = PayRecord(blueprint['category'], blueprint['value'],
                                blueprint['comment'])

                # incrementing ids
                self.record_id += 1
                pay.last_id += self.record_id
                pay.sign = '-'
                self.account['last_record_id'] = self.record_id

                # when we pay, account always decreasing
                # it's up to Credit class to identify
                # that '-' means increase debt
                # or we can specify credit limit and
                # show limit - value in view
                self.account[blueprint['category']].value -= \
                    int(blueprint['value'])
                self.account['payments'].put_payment(pay)

                # we always making snapshow in history
                # and alway save pickle file
                self.__snapshot_history()
                self.__save()
                return msg.pay_message
        else:
            return msg.pay_error

    def income(self, params):
        self.logger.debug("Great, we got money now")
        blueprint = self.prs.income_check(params)
        if blueprint:
            if blueprint['category'] not in category_list:
                return msg.income_category_error
            else:
                income = PayRecord(blueprint['category'], blueprint['value'],
                                   blueprint['comment'])

                self.record_id += 1
                income.last_id += self.record_id
                income.sign = '+'
                self.account['last_record_id'] = self.record_id

                # when we got money it's alway '+'
                # and it's also up to Credit account to
                # parse it as debt decreasing
                self.account['payments'].put_payment(income)
                self.account[blueprint['category']].value += \
                    int(blueprint['value'])

                self.__snapshot_history()
                self.__save()
                return msg.income_message
        else:
            return msg.income_error

    def withdraw(self, params):
        self.logger.debug("Taking money from acoount to cash")
        blueprint = self.prs.withdraw_check(params)
        if blueprint:
            if blueprint['category'] not in withdraw_category_list:
                return msg.withdraw_category_error
            else:
                pay = PayRecord(blueprint['category'], blueprint['value'],
                                "withdraw")

                self.record_id += 1
                pay.last_id += self.record_id
                self.account['last_record_id'] = self.record_id

                # withdraw is alway taking money from any account
                # into cash
                # therefore, we check limit and check
                self.account['payments'].put_payment(pay)
                self.account[blueprint['category']].value -= \
                    int(blueprint['value'])
                self.account['cash'].value += int(blueprint['value'])

                self.__snapshot_history()
                self.__save()
                return msg.succes_withdraw_message
        else:
            return msg.withdraw_error
        return msg.withdraw_message

    # sync method to update pickle file
    def __save(self):
        self.logger.debug("Saving all to pickle file")
        with open(self.account['name'] + ".pickle", 'wb') as f:
            pickle.dump(self.account, f, -1)
        return msg.save_message

    # sync method place stats for balance history
    def __snapshot_history(self):
        self.logger.debug("Updating balance history")
        last_record = BalanceRecord(self.account['cash'].value,
                                    self.account['debit'].value,
                                    self.account['credit'].value,
                                    self.account['savings'].value,)
        self.account['history'].put_record(last_record)

        # here we never just call snapshot_history_message
        # without doing nothing
        # alway payment, or withdraw or income
        last_record.last_id = self.record_id
        return msg.snapshot_history_message


class Bus(object):
    '''This class corresponds for output format for any consumers'''

    # use our logger metaclass
    __metaclass__ = CmdLog

    def __init__(self):
        self.logger.debug("Created data bus device")

    def slow_type(self, message):
        '''human typing style function to make printing pretty'''
        typing_delay = 300
        for ch in message:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(random.random() * 10.0 / typing_delay)
        print ''

    def send_data(self, cls, cmd):
        '''dispatcher of commands to CmdMux class'''
        action = cmd.split()[0]
        # we do not need actually to call regexp here
        # method of Mux will parse params and validate them
        # and send appropriate message
        try:
            if action in static_commands:
                result_message = getattr(cls, action)()
            else:
                result_message = getattr(cls, action)(cmd)
            self.slow_type(result_message)
        except AttributeError:
            print("there is not such command: {0}..try again!".format(action))
