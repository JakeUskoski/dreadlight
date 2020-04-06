import json

from dreadlight.data import store


class Purse:
    def __init__(self):
        self.__coin_purse = {}

    @staticmethod
    def load_purse(purse_dictionary):
        purse = Purse()
        purse.__coin_purse = purse_dictionary
        return purse

    def gain_currency(self, currency, amount):
        if amount <= 0:
            return
        old_value = self.__coin_purse.get(currency)
        if old_value is None:
            old_value = 0

        self.__coin_purse[currency] = old_value + amount

    def lose_currency(self, currency, amount):
        if amount <= 0:
            return
        old_value = self.__coin_purse.get(currency)
        if old_value is None:
            return
        elif old_value <= amount:
            self.__coin_purse.pop(currency)
        else:
            self.__coin_purse[currency] = old_value - amount

    def get_currency(self, currency):
        old_value = self.__coin_purse.get(currency)
        if old_value is None:
            old_value = 0
        return old_value

    def get_held_currencies(self):
        return list(self.__coin_purse.keys())

    def __str__(self):
        string = '{'
        if len(self.get_held_currencies()) > 0:
            for currency in self.get_held_currencies():
                string += '"' + currency + '": ' + str(self.get_currency(currency)) + ", "
            string = string[:-2]

        return string + '}'


if __name__ == '__main__':
    some_purse = Purse()
    some_purse.gain_currency('Shuckles', 250)
    some_purse.gain_currency('Grimes', 86)
    some_purse.gain_currency('Glints', 3)
    print(some_purse)
    some_purse_dictionary = json.loads(str(some_purse))
    print(str(some_purse_dictionary))
    duplicate_data = Purse.load_purse(some_purse_dictionary)
    print(str(duplicate_data))
    store.store_purse(some_purse)
