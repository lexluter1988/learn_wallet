from controls import CmdMux
from controls import Bus

# instantiate you Commands Multiplexer and Data/Commands bus
# it will take all commands and return results
# from appropriate methods
# primary entry point for program
mux = CmdMux()
bus = Bus()

# global quit variable
quit_recieved = False

# infinite loop till KeyboardInterrupt
# or 'quit' command
bus.send_data(mux, 'hello')

while not quit_recieved:
    try:
        command = raw_input("prompt> ")
        if not command:
            continue
        # we can affort to send messages for tutor and help
        # even if he have not account yet
        elif (lambda x: isinstance(x, str)
              and (x.startswith("help")
                   or x.startswith("tutorial")
                   or x.startswith("new_account")
                   or x.startswith("open_account")))(command):
            bus.send_data(mux, command)
        # also we allow to quit from program, obviously
        elif (lambda x: isinstance(x, str) and x.startswith("quit"))(command):
            break
        # and then we check if user have or not any account
        elif not mux.account_opened:
            bus.send_data(mux, 'no_account')
        # simply exit with no call to multiplexer
        else:
            # we just send string to multiplexer
            # there we will parse and take arguments
            # main.py is just like console for user
            # all internal calculations are hided
            bus.send_data(mux, command)
    except KeyboardInterrupt:
        bus.send_data(mux, 'quit')
        exit(0)

bus.send_data(mux, 'quit')
