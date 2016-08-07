from controls import CmdMux
import time
import random
import sys


# instantiate you Commands Multiplexer
# it will take all commands and return results
# from appropriate methods
inst = CmdMux()


def slow_type(message):
    '''human typing style function to make printing pretty'''
    typing_delay = 50
    for ch in message:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(random.random() * 10.0 / typing_delay)
    print ''


def proceed(cmd):
    '''dispatcher of commands to CmdMux class'''
    try:
        result_message = getattr(inst, cmd)()
        slow_type(result_message)
    except AttributeError:
        print("there is not such command: {0}..try again!".format(cmd))


# global quit variable
quit_recieved = False

# entry point for program
# infinite loop till KeyboardInterrupt
# or 'quit' command
while not quit_recieved:
    try:
        command = raw_input("prompt> ")
        if command.lower.startswith("quit"):
            break
        else:
            proceed(command)
    except KeyboardInterrupt:
        print(" goodbye fella!")
        exit(0)
