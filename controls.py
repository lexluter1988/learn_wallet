import logging
import sys
import time
import random
from messages import Messages as msg
from accounts import Cash, Debit, Credit, Savings
import cPickle as pickle
from memory import BalanceHistory, BalanceRecord, PayHistory, PayRecord


# tuple of commands we can call with no arguments
# commands like getters of values
# no arguments needed here
static_commands = (
    'hello',
    'help',
    'tutorial',
    'save',
    'quit',
    'cash',
    'balance',
    'debit',
    'credit',
    'no_account',
    )

# tuple of commands which take exact one argument
# example 1: new_account wallet cash=100 debit=0 credit=0 savings=0
# example 2: open_account wallet
# example 3: pay cash 1000 bitches
# example 4: withdraw credit 100
# example 5: history 100
operation_list = (
    'new_account',
    'open_account',
    'pay',
    'withdraw',
    )

history_list = (
    'history',
    'payments',
    )


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
        self.account_opened = False
        self.logger.debug("Created multiplexer for user's commands")

    # account initiation methods
    def no_account(self):
        self.logger.debug("no account opened")
        return msg.no_account_message

    def new_account(self, params):
        self.logger.debug("Creating new clean account")
        if params:
            # shortest way for now
            # to parse input despite of order
            try:
                for i in params:
                    if i.startswith("name="):
                        name = i.split('=')[1]
                    elif i.startswith("cash="):
                        cash = i.split('=')[1]
                    elif i.startswith("debit="):
                        debit = i.split('=')[1]
                    elif i.startswith("credit="):
                        credit = i.split('=')[1]
                    elif i.startswith("savings="):
                        savings = i.split('=')[1]
                    else:
                        self.logger.error("Not all parameters specified")
                        return "FAILED"
            except:
                self.logger.error("Invalid input parameters")
                return "FAILED"
        else:
            self.logger.debug("Empty parameters for account")
            return "FAILED"
        # since all store(cash, debit, credit, savings) are
        # secure, I do not assgin values on instance creation
        # only by setters

#        if not all(i is not None and isinstance(i, str) for i in
#                   [name, cash, debit, credit, savings]):
# cannot check cause
# UnboundLocalError: local variable 'cash' referenced before assignment
            self.logger.debug("Empty parameters for account")
            return "FAILED"

        tmp_cash = Cash()
        tmp_cash.value = int(cash)

        tmp_debit = Debit()
        tmp_debit.value = int(debit)

        tmp_credit = Credit()
        tmp_credit.value = int(credit)

        tmp_savings = Savings()
        tmp_savings.value = int(savings)

        self.account = {'name': name,
                        'cash': tmp_cash,
                        'debit': tmp_debit,
                        'credit': tmp_credit,
                        'savings': tmp_savings,
                        'balance_history': BalanceHistory(),
                        'payments_history': PayHistory(),
                        }
        self.__save()
        self.account_opened = True
        return msg.new_account_message

    def open_account(self, params):
        print(params)
        self.logger.debug("Opening your account")
        self.account_opened = True
        return msg.open_account_message
        self.account

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
        return msg.balance_message

    def cash(self):
        self.logger.debug("Getting your cash")
        return msg.cash_message

    def debit(self):
        self.logger.debug("Getting your debit account")
        return msg.debit_message

    def credit(self):
        self.logger.debug("Getting your credit account")
        return msg.credit_message

    def savings(self):
        self.logger.debug("Getting your savings")
        return msg.savings_message

    # history methods, for last payments and balance history
    def history(self, params):
        print(params)
        self.logger.debug("Getting your last balance history")
        return msg.history_message

    def payments(self, params):
        print(params)
        self.logger.debug("Getting you last payments")
        return msg.payments_message

    # real operation methods
    def pay(self, params):
        print(params)
        self.logger.debug("Paying for something")
        return msg.pay_message

    def income(self, params):
        print(params)
        self.logger.debug("Great, we got money now")
        return msg.income_message

    def withdraw(self, params):
        print(params)
        self.logger.debug("Taking money from acoount to cash")
        return msg.withdraw_message

    # sync method to update pickle file
    def __save(self):
        self.logger.debug("Saving all to pickle file")
        with open(self.account['name']+".pickle", 'wb', -1) as f:
            pickle.dump(self.account, f)
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
        params = cmd.split()
        action = params.pop(0)
        try:
            if action in static_commands:
                result_message = getattr(cls, action)()
            else:
                result_message = getattr(cls, action)(params)
            self.slow_type(result_message)
        except AttributeError:
            print("there is not such command: {0}..try again!".format(action))
