from controls import CmdMux
from controls import Bus
from accounts import Cash, Debit, Credit, Savings
from memory import BalanceRecord, PayRecord

# instantiate you Commands Multiplexer
# it will take all commands and return results
# from appropriate methods
mux = CmdMux()
bus = Bus()

cash = Cash()
cash.value = 1
debit = Debit()
debit.value = 16000
credit = Credit()
credit.value = -150000
savings = Savings()
savings.value = 71000
one_record = PayRecord()
one_history = BalanceRecord()

record = {'cash': cash,
          'debit': debit,
          'credit': credit,
          'savings': savings,
          'history': [one_history, ],
          'records': [one_record, ],
          }

# print(record)

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
        elif (lambda x: isinstance(x, str) and x.startswith("quit"))(command):
            break
        else:
            bus.send_data(mux, command, record)
    except KeyboardInterrupt:
        bus.send_data(mux, 'quit')
        exit(0)

bus.send_data(mux, 'quit')
