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
        self.logger.debug("Created multiplexer for user's commands")

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

    def balance(self, record):
        self.logger.debug("Getting current balance")
        cash_val = record[0]['cash'].value
        debit_val = record[0]['debit'].value
        credit_val = record[0]['credit'].value
        savings_val = record[0]['savings'].value
        out = "Cash:{0} | Credit:{1} | Debit:{2} | Savings:{3}\n{4}".format(
            cash_val, debit_val, credit_val, savings_val, msg.balance_message)
        return out


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

    def send_data(self, cls, cmd, *args):
        '''dispatcher of commands to CmdMux class'''
        try:
            if cmd == 'balance':
                result_message = getattr(cls, cmd)(args)
            else:
                result_message = getattr(cls, cmd)()
            self.slow_type(result_message)
        except AttributeError:
            print("there is not such command: {0}..try again!".format(cmd))
