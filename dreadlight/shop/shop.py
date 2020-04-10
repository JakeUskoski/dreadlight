import json

from dreadlight.data import store


class Shop:
    def __init__(self, store_owner, currency):
        self.store_owner = store_owner
        self.currency = currency
        self.items_for_sale = {}
        self.items_for_purchase = {}

    @staticmethod
    def load_shop(data_dictionary):
        store_data = Shop(data_dictionary['store_owner'], data_dictionary['currency'])
        store_data.items_for_sale = data_dictionary['items_for_sale']
        store_data.items_for_purchase = data_dictionary['items_for_purchase']
        return store_data

    def add_item_for_sale(self, item_name, cost):
        self.items_for_sale[item_name] = cost

    def get_item_for_sale_at_index(self, index):
        items = self.get_items_for_sale_list()
        if 0 < index < len(items):
            return items[index]

    def get_item_for_sale_cost_by_index(self, index):
        index -= 1
        items = self.get_items_for_sale_list()
        if 0 < index < len(items):
            return self.get_item_for_sale_cost(items[index])

    def get_item_for_sale_cost(self, item_name):
        return self.items_for_sale.get(item_name)

    def get_items_for_sale_list(self):
        return list(self.items_for_sale.keys())

    def add_item_for_purchase(self, item_name, purchase_price):
        self.items_for_purchase[item_name] = purchase_price

    def get_item_for_purchase_at_index(self, index):
        items = self.get_items_for_purchase_list()
        if 0 < index < len(items):
            return items[index]

    def get_item_for_purchase_cost_by_index(self, index):
        index -= 1
        items = self.get_items_for_purchase_list()
        if 0 < index < len(items):
            return self.get_item_for_purchase_cost(items[index])

    def get_item_for_purchase_cost(self, item_name):
        return self.items_for_purchase.get(item_name)

    def get_items_for_purchase_list(self):
        return list(self.items_for_purchase.keys())

    def __str__(self):
        string = '{"store_owner": "' + self.store_owner + '"' + \
                 ', "currency": "' + self.currency + '"' + \
                 ', "items_for_sale": {'

        if len(self.get_items_for_sale_list()) > 0:
            for item in self.get_items_for_sale_list():
                string += '"' + item + '": ' + str(self.items_for_sale[item]) + ", "
            string = string[:-2]

        string += '}, "items_for_purchase": {'

        if len(self.get_items_for_purchase_list()) > 0:
            for item in self.get_items_for_purchase_list():
                string += '"' + item + '": ' + str(self.items_for_purchase[item]) + ", "
            string = string[:-2]

        return string + '}}'
