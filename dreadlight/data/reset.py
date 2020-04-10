import os
import shutil

from dreadlight.common import utils
from dreadlight.data import paths


def __remove(directory, filename):
    full_path = os.path.join(directory, filename)
    try:
        if not os.path.exists(full_path):
            return
        elif os.path.isfile(full_path):
            os.remove(full_path)
        else:
            shutil.rmtree(full_path)
    except OSError as e:
        print("Error: %s : %s" % (full_path, e.strerror))


def inventory():
    __remove(paths.SAVE_DIR, 'inventory')


def purse():
    __remove(paths.SAVE_DIR, 'purse')


def item(item_name):
    __remove(paths.ITEMS_DIR, utils.normalize_caseless(item_name))


def items():
    __remove(paths.ITEMS_DIR, '')


def player_class(class_name):
    __remove(paths.CLASSES_DIR, utils.normalize_caseless(class_name))


def classes():
    __remove(paths.CLASSES_DIR, '')


def shop(shop_name):
    __remove(paths.SHOPS_DIR, utils.normalize_caseless(shop_name))


def shops():
    __remove(paths.SHOPS_DIR, '')


def player():
    __remove(paths.SAVE_DIR, 'player')
