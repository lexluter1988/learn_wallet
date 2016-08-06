import logging
import sys


class CmdLog(type):

    def __new__(cls, name, bases, namespace, **kwargs):
        result = type.__new__(cls, name, bases, dict(namespace))
        # changing logger to strdout
        out_handler = logging.StreamHandler(sys.stdout)
        # format for output

        out_handler.setFormatter(logging.Formatter(
                '%(asctime)s [%(levelname)s] [%(name)s] - %(message)s'))
        out_handler.setLevel(logging.DEBUG)

        # adjust out logger
        result.logger = logging.getLogger(name)
        result.logger.addHandler(out_handler)
        result.logger.setLevel(logging.DEBUG)

        return result


class CheckMeta(object):
    __metaclass__ = CmdLog

    def __init__(self, value):
        self.value = value
        self.logger.debug("testing logger, value is {0}".format(value))

    def show_logs(self):
        self.logger.info("hello child, you said {0}".format(self.value))


class CmdMux(object):
    '''This is main control unit, sends command to all units'''
    commands_list = (
        'empty-wallet',
        'record-payment',
        'get-balance',
    )

    def __init__(self):
        pass


class OutDevice(object):
    '''This class corresponds for output format for any consumer'''

    def __init__(self):
        pass
