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
                   'savings', )

# allowed category tuple
category_list = ('cash',
                 'debit',
                 'credit',
                 'savings', )

# tuple of commands which take exact one argument
# example 1: new_account name=wallet cash=100 debit=0 credit=0 savings=0
# example 2: open_account name=wallet
# example 3: pay category=cash value=1000 comment=bitches
# example 4: withdraw category=credit value=100
# example 5: history records=100
operation_list = ('new_account',
                  'open_account',
                  'pay',
                  'withdraw',
                  'income', )

history_list = ('history',
                'payments', )


class CmdLog(type):
    '''Commands logger metaclass, used only for commands'''

    def __new__(cls, name, bases, namespace, **kwargs):
        # basic metaclass override of new method
        result = type.__new__(cls, name, bases, dict(namespace))
        # changing logger to strdout
        out_handler = logging.StreamHandler(sys.stdout)

        # format logger to write in stdout
        # we write in format like:
        # '1970-01-10, 15:49:12,913 [INFO] [CheckMeta] - Hello World!'
        out_handler.setFormatter(logging.Formatter(
            '%(asctime)s [%(levelname)s] [%(name)s] - %(message)s'))
        out_handler.setLevel(logging.DEBUG)

        # adjust our metaclass to contain logger from beginning
        result.logger = logging.getLogger(name)
        result.logger.addHandler(out_handler)
        result.logger.setLevel(logging.DEBUG)

        return result


class CmdMux(object):
    '''This is the main control unit, sends command to all units'''
    # use our logger metaclass
    __metaclass__ = CmdLog

    def __init__(self):
        self.prs = Parsers()
        self.account_opened = False
        self.logger.debug("Created multiplexer for user's commands")

    # account initiation methods
    def no_account(self):
        self.logger.debug("no account opened")
        return msg.no_account_message

    def new_account(self, params):
        self.logger.debug("Creating new clean account")
        # shortest way for now
        # to parse input despite of order
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

            tmpcash, tmpdebit, tmpcredit, tmpsavings = \
                Cash(), Debit(), Credit(), Savings()

            tmppayments, tmphistory = PayHistory(), BalanceHistory()

            # assigning values
            tmpcash.value = int(blueprint['cash'])
            tmpdebit.value = int(blueprint['debit'])
            tmpcredit.value = int(blueprint['credit'])
            tmpsavings.value = int(blueprint['savings'])

            # saving complete object (since new account, everything is empty)
            self.account = {
                'name': tmpname,
                'cash': tmpcash,
                'debit': tmpdebit,
                'credit': tmpcredit,
                'savings': tmpsavings,
                'payments': tmppayments,
                'history': tmphistory,
            }
            self.__save()
            return msg.new_account_message
        else:
            return msg.basic_input_error

    def open_account(self, params):
        self.logger.debug("Opening your account")
        account_name = self.prs.open_account_check(params)
        if account_name:
            try:
                with open(account_name + '.pickle', 'rb') as f:
                    # in fact we load everything quite easy
                    # into object so all methods can work with it
                    # anyway we work only from cmd mux
                    self.account = pickle.load(f)
                    self.account_opened = True
                    return msg.open_account_message
            except TypeError:
                self.logger.error("Failure during opening")
                return msg.basic_input_error
            except IOError:
                self.logger.error("Account does not exist")
                return msg.basic_input_error
        else:
            self.account_opened = False
            return msg.basic_input_error

    # info methods that do not need any value or calculation
    def hello(self):
        self.logger.debug("Entering into programm")
        return msg.hello_message

    def quit(self):
        self.logger.debug("Exiting from programm")
        return msg.quit_message

    def help(self):
        self.logger.debug("Asking for help")
        return msg.help_message

    def tutorial(self):
        self.logger.debug("Asking for tutorial")
        return msg.tutorial_message

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
        return msg.history_message

    def payments(self, params):
        self.logger.debug("Getting you last payments")
        return msg.payments_message

    # real operation methods
    def pay(self, params):
        self.logger.debug("Paying for something")
        blueprint = self.prs.pay_check(params)
        if blueprint:
            money_i_have = self.account[blueprint['category']].value
            if blueprint['category'] not in category_list:
                return msg.pay_category_error
            elif (int(blueprint['value']) > int(money_i_have)):
                return msg.pay_no_money_error
            else:
                pay = PayRecord(blueprint['category'], blueprint['value'],
                                blueprint['comment'])
                pay.last_id += 1
                self.account['payments'].put_payment(pay)
                self.account[blueprint['category']].value -= \
                    int(blueprint['value'])
                self.__save()
                return msg.pay_message
        else:
            return msg.basic_input_error

    def income(self, params):
        self.logger.debug("Great, we got money now")
        return msg.income_message

    def withdraw(self, params):
        self.logger.debug("Taking money from acoount to cash")
        return msg.withdraw_message

    # sync method to update pickle file
    def __save(self):
        self.logger.debug("Saving all to pickle file")
        with open(self.account['name'] + ".pickle", 'wb') as f:
            pickle.dump(self.account, f, -1)
        return msg.save_message


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
