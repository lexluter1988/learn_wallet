from controls import CmdMux
from controls import Bus

# instantiate you Commands Multiplexer and Data/Commands bus
# it will take all commands and return results
# from appropriate methods
mux = CmdMux()
bus = Bus()

account_inited = mux.account_opened
# global quit variable
quit_recieved = False

# entry point for program
# infinite loop till KeyboardInterrupt
# or 'quit' command
bus.send_data(mux, 'hello')

while not quit_recieved:
    try:
        command = raw_input("prompt> ")
        if not command:
            continue
        elif not account_inited:
            bus.send_data(mux, 'no_account')
        # simply exit with no call to multiplexer
        elif (lambda x: isinstance(x, str) and x.startswith("quit"))(command):
            break
        else:
            # we just send string to multiplexer
            # ther we will parse and take arguments
            # main file is just like console for user
            # all internal calculations are hided
            bus.send_data(mux, command)
    except KeyboardInterrupt:
        bus.send_data(mux, 'quit')
        exit(0)

bus.send_data(mux, 'quit')
