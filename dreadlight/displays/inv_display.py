from dreadlight.common import utils
from dreadlight.data import loader
from dreadlight.displays.commons import LINE_BREAK, print_purse, print_list, print_item_details, print_item_comparison
from dreadlight.player import inventory


def inv_list():
    items = inventory.get_inventory_list()
    coin_purse = loader.load_purse()
    print()
    print('COIN PURSE')
    print(LINE_BREAK)
    print_purse(coin_purse)
    print()
    print('INVENTORY')
    print(LINE_BREAK)
    if items:
        print_list(items)
    else:
        print('Your inventory is empty...')
    print()


def inv_details(item_reference):
    inventory_item = inventory.get_details_of_item(item_reference)
    if not inventory_item:
        item_not_found(item_reference)
    else:
        print_item_details(inventory_item)


def inv_compare(item_reference, other_item_reference):
    inventory_item = inventory.get_details_of_item(item_reference)
    compared_inventory_item = inventory.get_details_of_item(other_item_reference)
    item = inventory_item.item
    compared_item = compared_inventory_item.item

    if not item:
        item_not_found(item_reference)
    if not compared_item:
        item_not_found(other_item_reference)

    if item and compared_item:
        item_equipped = inventory_item.is_equipped
        compared_item_equipped = compared_inventory_item.is_equipped
        print_item_comparison(item, compared_item, item_equipped, compared_item_equipped)


def inv_toss(item_references):
    removals, failures = inventory.toss_items(item_references)
    print()
    print('REMOVED')
    print(LINE_BREAK)
    if removals:
        print_list(removals)
    else:
        print('Nothing was successfully removed.')
    print()
    if failures:
        print('ERRORS')
        print(LINE_BREAK)
        for ref in failures:
            item_not_found(ref)
        print()


def inv_equip(item_reference):
    already_equipped = inventory.equip_item(item_reference)
    if already_equipped is None:
        print('Equipped successfully!')
    elif not already_equipped:
        item_not_found(item_reference)
    else:
        inventory_item = inventory.get_details_of_item(item_reference)
        if inventory_item.is_equipped:
            print("Couldn't equip. It's already equipped.")
        else:
            print("Couldn't equip. Unequip the following first:")
            for item in already_equipped:
                print(item.name)


def inv_unequip(item_reference):
    if inventory.unequip_item(item_reference):
        print('Unequipped successfully!')
    else:
        inventory_item = inventory.get_details_of_item(item_reference)
        if not inventory_item:
            item_not_found(item_reference)
        elif not inventory_item.is_equipped:
            print(inventory_item.item.name + " isn't equipped.")
        else:
            print('Unexpected error occurred.')


def item_not_found(item_name):
    if utils.is_int(item_name):
        print('Position ' + str(item_name) + ' out of inventory bounds.')
    else:
        print('Item "' + item_name + '" could not be found in your inventory.')
