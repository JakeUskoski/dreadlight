import os

from dreadlight.common import utils
from dreadlight.data import paths


def __write_to_file(obj, path, filename):
    file = open(os.path.join(path, utils.normalize_caseless(filename)), 'w+')
    file.write(str(obj))
    file.close()


def store_item(item):
    __write_to_file(item, paths.ITEMS_DIR, utils.normalize_caseless(item.name))


def store_class(class_obj):
    __write_to_file(class_obj, paths.CLASSES_DIR, utils.normalize_caseless(class_obj.name))


def store_inventory(inventory_items):
    string_inventory = '{"inventory":['
    if inventory_items:
        for item in inventory_items:
            string_inventory += str(item) + ','
        string_inventory = string_inventory[0:-1]
    string_inventory += ']}'
    __write_to_file(string_inventory, paths.SAVE_DIR, 'inventory')


def store_shop(shop):
    __write_to_file(shop, paths.SHOPS_DIR, shop.store_owner)


def store_player(player):
    __write_to_file(player, paths.SAVE_DIR, 'player')


def store_purse(purse):
    __write_to_file(purse, paths.SAVE_DIR, 'purse')
