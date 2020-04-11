from functools import reduce


class Purse:
    def __init__(self):
        self.__coin_purse = {}

    @staticmethod
    def load_purse(purse_dictionary):
        purse = Purse()
        purse.__coin_purse = purse_dictionary
        return purse

    def gain_currency(self, currency, amount):
        if int(amount) <= 0:
            return
        old_value = self.__coin_purse.get(currency)
        if old_value is None:
            old_value = 0

        self.__coin_purse[currency] = int(old_value) + int(amount)

    def lose_currency(self, currency, amount):
        if int(amount) <= 0:
            return
        old_value = self.__coin_purse.get(currency)
        if old_value is None:
            return
        elif int(old_value) <= amount:
            self.__coin_purse.pop(currency)
        else:
            self.__coin_purse[currency] = int(old_value) - int(amount)

    def get_currency(self, currency):
        old_value = self.__coin_purse.get(currency)
        if old_value is None:
            old_value = 0
        return int(old_value)

    def get_held_currencies(self):
        return list(self.__coin_purse.keys())

    def __str__(self):
        string = '{'
        if len(self.get_held_currencies()) > 0:
            for currency in self.get_held_currencies():
                string += '"' + currency + '": ' + str(self.get_currency(currency)) + ", "
            string = string[:-2]

        return string + '}'
