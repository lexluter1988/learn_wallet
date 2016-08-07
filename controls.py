import logging
import sys
import time
import random
from messages import Messages as msg


# tuple of commands we can call, global and static
commands_list = (
    'help',
    'tutorial',
    'quit',
    'init',
    'balance',
    'debit',
    'credit',
    'payments',
    'history',
    'withdraw',
    'pay',
    'save',
    'open_account',
    'new_account',
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

    def new_account(self):
        self.logger.debug("Creating new clean account")
        self.account_opened = True
        return msg.new_account_message

    def open_account(self):
        self.logger.debug("Opening your account")
        self.account_opened = True
        return msg.open_account_message

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
    def history(self, records=10):
        self.logger.debug("Getting your last balance history")
        return msg.history_message

    def payments(self, records=10):
        self.logger.debug("Getting you last payments")
        return msg.payments_message

    # real operation methods
    def pay(self, category=cash, value=0):
        self.logger.debug("Paying for something")
        return msg.pay_message

    def income(self, category=cash, value=0):
        self.logger.debug("Great, we got money now")
        return msg.income_message

    def withdraw(self, value=0):
        self.logger.debug("Taking money from acoount to cash")
        return msg.withdraw_message

    # sync method to update pickle file
    def save(self):
        self.logger.debug("Saving all to pickle file")
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
        to_do = params[0]
        try:
            result_message = getattr(cls, to_do)()
            self.slow_type(result_message)
        except AttributeError:
            print("there is not such command: {0}..try again!".format(cmd))
