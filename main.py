from controls import CmdMux
import time
import random
import sys


inst = CmdMux()


def slow_type(message):
    # delay for typing
    typing_speed = 50
    for ch in message:
        sys.stdout.write(message)
        sys.stdout.flush()
        time.sleep(random.random() * 10.0 / typing_speed)
    print ''


def proceed(cmd):
    try:
        result_message = getattr(inst, cmd)()
        slow_type(result_message)
    except AttributeError:
        print("there is not such command: {0}..try again!".format(cmd))

print("let's play a game")

quit_recieved = False

while not quit_recieved:
    try:
        command = raw_input("prompt> ")
        proceed(command)
    except KeyboardInterrupt:
        print(" goodbye fella!")
        exit(0)
