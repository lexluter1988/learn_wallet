import logging
import sys
from messages import Messages as msg


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
    'pay',
    'quit',
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
        self.logger.debug("Asking for help")
        return msg.help_message

    def tutorial(self):
        self.logger.debug("Asking for tutorial")
        return msg.tutorial_message

    def quit(self):
        self.logger.debug("Got quit request, finishing programm")
        return msg.quit_message


class OutDevice(object):
    '''This class corresponds for output format for any consumers'''

    # use our logger metaclass
    __metaclass__ = CmdLog

    def __init__(self):
        pass
