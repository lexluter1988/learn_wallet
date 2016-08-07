from controls import CmdMux
from controls import OutDevice

# instantiate you Commands Multiplexer
# it will take all commands and return results
# from appropriate methods
mux = CmdMux()
out = OutDevice()

# global quit variable
quit_recieved = False

# entry point for program
# infinite loop till KeyboardInterrupt
# or 'quit' command
out.send_data(mux, 'hello')

while not quit_recieved:
    try:
        command = raw_input("prompt> ")
        if not command:
            continue
        elif (lambda x: isinstance(x, str) and x.startswith("quit"))(command):
            break
        else:
            out.send_data(mux, command)
    except KeyboardInterrupt:
        out.send_data(mux, 'quit')
        exit(0)

out.send_data(mux, 'quit')
