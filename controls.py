import logging


class CmdMux(object):
    '''This is main control unit, sends command to all units'''
    commands_list = (
        'empty-wallet',
        'record-payment',
        'get-balance',
    )

    def __init__(self):
        pass


class CmdLog(type):

    def __new__(cls, name, bases, namespace, **kwargs):
        result = type.__new__(cls, name, bases, dict(namespace))
        result.logger = logging.getLogger(name)
        return result


class CheckMeta(object):
    __metaclass__ = CmdLog

    def __init__(self, value):
        self.logger.info("testing logger, value is {0}".format(value))


class OutDevice(object):
    '''This class corresponds for output format for any consumer'''

    def __init__(self):
        pass
