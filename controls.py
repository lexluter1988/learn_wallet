import logging
import sys


# tuple of commands we can call, global and static
commands_list = (
    'help',
    'tutorial',
    'erase',
    'wallet',
    'balance',
    'debit',
    'credit',
    'payments',
    'history',
    'withdraw',
    'record-payment',
    'quit',
    )

help_message = '''
Welcome to the Fucking Wallet!
Go on tutorial by typing \'tutorial'
Or just ask 'help' to list all the commands

Start by initiating your empty wallet #looser
\'erase\'
Then go and put something into your cash (cash)
Then go and put some credit (credit), debit(debit)

And if you are so lucky and have some savings
Go the put some savings (saving)

List your balance (balance)
And see your history (history)

And then you can go and spend deeze nuts!
Good luck!
'''


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


class CheckMeta(object):
    '''Just an useless class for checking metaclass and logger'''
    __metaclass__ = CmdLog

    def __init__(self, value):
        self.value = value
        self.logger.debug("testing logger, value is {0}".format(value))

    def show_logs(self):
        self.logger.info("hello child, you said {0}".format(self.value))


class CmdMux(object):
    '''This is the main control unit, sends command to all units'''

    # use our logger metaclass
    __metaclass__ = CmdLog

    def __init__(self):
        self.logger.debug("Created multiplexer for user's commands")

    def help(self):
        self.logger.debug("Asking for help message")
        return help_message

    def quit(self):
        self.logger.debug("Got quit request, finishing programm")
        message = "got guit signal"
        return message


class OutDevice(object):
    '''This class corresponds for output format for any consumers'''

    # use our logger metaclass
    __metaclass__ = CmdLog

    def __init__(self):
        pass
