import sys
import time
import random


class Api(object):
    '''class from poaupdater who uses getattr to execute method
        based on string input name '''

# sub_id = int(sys.argv[1])
# connection = connect_via_rpc("192.168.133.12")
# api = Api(connection)
# responce = get_resource_usage_for_period(sub_id,api)
# return api.execute('pem.getResourceUsageForPeriod', **params)

    def __init__(self, connection):
        self.connection = connection

    def execute(self, method, **params):
        response = getattr(self.connection, method)(
            params)  # Hack from poaupdater
        if response['status'] != 0:
            self.txn_id = None
            raise Exception('Method {0} returned non-zero status {1} and\
                             error {2}'.format(method, response['status'],
                                               response['error_message']))
        else:
            return response.get('result', None)

# usefully for waiting inputs
# and proceed them as commands
got_quit = False


def proceed(cmd):
    if not cmd:
        return False
    elif cmd.lower().startswith("quit"):
        return True
    else:
        return False

while not got_quit:
    # in python 2 need to use raw_input instead of input
    # or we got ints, emptys, and eventually got
    # SyntaxError: unexpected EOF while parsing
    command = raw_input("====> ")
    got_quit = proceed(command)


def slow_type(t):
    # delay for typing
    typing_speed = 50
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random() * 10.0 / typing_speed)
    print ''

# need to move messages and
# help to separate files
message = '''
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
slow_type(message)
