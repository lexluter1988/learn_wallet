from balancerecord import BalanceRecord
import cPickle as pickle


class BalanceHistory(object):
    '''This is imutable memory unit, containing balance history'''

    def __init__(self):
        pass

    def save_a_lot(self):
        biig = []
        for i in range(1000000):
            itemm = BalanceRecord(i)
            biig.append(itemm)

        with open('records.pickle', 'wb') as f:
            pickle.dump(biig, f, -1)

# just perfectly saved and loaded
# list stores array of our needed objects ideally
