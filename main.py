print("you entered into game")
quit_recieved = False
while not quit_recieved:
    command = str(input("prompt> "))
# not working: NameError: name 'sfh' is not defined
    print(command)
    quit_recieved = (lambda x: x.startswith("quit"))(command)

print("fuck you!")

# except KeyboardInterrupt:
#    print("well, fuck you asshole!")
