import sys
import time
import random

# wpm
typing_speed = 50


def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random() * 10.0 / typing_speed)
    print ''

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
