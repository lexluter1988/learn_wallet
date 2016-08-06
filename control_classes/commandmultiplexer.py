class CommandMultiplexer(object):
    '''This is main control unit, sends command to all units'''
    commands_list = (
        'empty-wallet',
        'record-payment',
        'get-balance',
    )

    def __init__(self):
        pass
