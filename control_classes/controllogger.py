import logging


class ControlLogger(type):

    def __new__(cls, name, bases, namespace, **kwargs):
        result = type.__new__(cls, name, bases, dict(namespace))
        result.logger = logging.getLogger(name)
        return result


class CheckMeta(object):
    __metaclass__ = ControlLogger

    def __init__(self, value):
        self.logger.info("testing logger, value is {0}".format(value))
