import json
import os

from dreadlight.common import utils
from dreadlight.common.character import Character
from dreadlight.common.item import Item, InventoryItem
from dreadlight.common.playable_class import PlayableClass
from dreadlight.data import paths
from dreadlight.player.purse import Purse
from dreadlight.shop.shop import Shop


def __load_dictionary(filename):
    file = open(utils.normalize_caseless(filename), 'r')
    dictionary = json.loads(file.read())
    file.close()
    return dictionary


def __check_file(filename):
    return os.path.exists(filename) and os.path.isfile(filename)


def load_class(class_name):
    filename = os.path.join(paths.CLASSES_DIR, utils.normalize_caseless(class_name))
    if not __check_file(filename):
        return None
    return PlayableClass.load_class(__load_dictionary(filename))


def load_all_classes():
    classes = []
    class_refs = os.listdir(paths.CLASSES_DIR)
    for ref in class_refs:
        classes.append(load_class(ref))
    return classes


def load_item(item_name):
    filename = os.path.join(paths.ITEMS_DIR, utils.normalize_caseless(item_name))
    if not __check_file(filename):
        return None
    return Item.load_item(__load_dictionary(filename))


def load_all_items():
    items = []
    item_refs = os.listdir(paths.ITEMS_DIR)
    for ref in item_refs:
        items.append(load_item(ref))
    return items


def load_inventory():
    filename = os.path.join(paths.SAVE_DIR, 'inventory')
    if not __check_file(filename):
        return []
    inventory = []
    for inv_item in __load_dictionary(filename)['inventory']:
        inventory.append(InventoryItem.load_item(inv_item))
    return inventory


def load_player():
    filename = os.path.join(paths.SAVE_DIR, 'player')
    if not __check_file(filename):
        return None
    return Character.load_character(__load_dictionary(filename))


def load_shop(shop_owner):
    filename = os.path.join(paths.SHOPS_DIR, shop_owner)
    if not __check_file(filename):
        return None
    return Shop.load_shop(__load_dictionary(filename))


def load_purse():
    filename = os.path.join(paths.SAVE_DIR, 'purse')
    if not __check_file(filename):
        return None
    return Purse.load_purse(__load_dictionary(filename))


if __name__ == '__main__':
    print(load_inventory())
