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
        print(" goodbye fella!")
        exit(0)
print(" goodbye fella!")
