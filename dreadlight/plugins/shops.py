from dreadlight.data import store, reset
from dreadlight.shop.shop import Shop


def reset_all():
    reset.shops()


def initialize():
    shop = Shop('Reolas', 'Shuckles')
    shop.add_item_for_sale('short sword', 130)
    shop.add_item_for_sale('kite shield', 150)
    shop.add_item_for_sale('cloth boots', 50)
    shop.add_item_for_purchase('short sword', 13)
    shop.add_item_for_purchase('kite shield', 15)
    shop.add_item_for_purchase('cloth boots', 5)
    store.store_shop(shop)
