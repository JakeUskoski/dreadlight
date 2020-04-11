from functools import reduce

from dreadlight.common import utils
from dreadlight.data import loader
from dreadlight.displays.commons import LINE_BREAK, print_list, print_item_details, print_item_comparison
from dreadlight.player import inventory


def shop_list():
    shop = __load_current_shop()
    goods = __construct_cost_list(shop)
    wants = __construct_purchase_list(shop, len(goods))
    coin_purse = loader.load_purse()

    print()
    print(shop.store_owner.upper() + "'S SHOP")
    print(LINE_BREAK)
    print('Accepted currency: ' + shop.currency)
    print('You currently have: ' + str(coin_purse.get_currency(shop.currency)) + ' ' + shop.currency)
    print()
    print('ITEMS FOR SALE')
    print(LINE_BREAK)
    if len(goods) > 0:
        print_list(goods)
    else:
        print(shop.store_owner + " isn't selling anything...")
    print()
    print('ITEMS DESIRED')
    print(LINE_BREAK)
    if len(wants) > 0:
        print_list(wants)
    else:
        print(shop.store_owner + " isn't buying anything...")
    print()
    print('CURRENT EQUIPMENT')
    print(LINE_BREAK)
    inventory_items = __append_count_to_item_list(map(lambda inv_item: inv_item.item, inventory.get_equipment()),
                                                  len(goods) + len(wants))
    if len(inventory_items) > 0:
        print_list(inventory_items)
    else:
        print("You don't have any items equipped.")
    print()


def shop_details(item_reference):
    shop = __load_current_shop()
    equipment = inventory.get_equipment()
    item, item_from = __get_item_from_shop(shop, equipment, item_reference)

    if not item:
        __item_not_found(item_reference)
    else:
        if item_from != 'equipment':
            item = loader.load_item(item)
        print_item_details(item)


def shop_compare(item_reference, compared_item_reference):
    shop = __load_current_shop()
    equipment = inventory.get_equipment()
    item, item_from = __get_item_from_shop(shop, equipment, item_reference)
    compared_item, compared_item_from = __get_item_from_shop(shop, equipment, compared_item_reference)

    if not item:
        __item_not_found(item_reference)
    if not compared_item:
        __item_not_found(compared_item_reference)

    if item and compared_item:
        item_equipped = item_from == 'equipment'
        compared_item_equipped = compared_item_from == 'equipment'

        if not item_equipped:
            item = loader.load_item(item)
        if not compared_item_equipped:
            compared_item = loader.load_item(compared_item)

        print_item_comparison(item, compared_item, item_equipped, compared_item_equipped)


def shop_buy(item_references):
    shop = __load_current_shop()
    item_purchases = []
    purse = loader.load_purse()

    for item_reference in item_references:
        item = __get_item_from_buy_list(shop, item_reference)
        if not item:
            __item_not_found(item_reference)
        else:
            item_purchases.append(item)

    if len(item_references) != len(item_purchases):
        print('The sale will not proceed without all requested items found.')
        print()
    else:
        total_cost = reduce(lambda item_name: shop.get_item_for_sale_cost(item_name), item_purchases)

        player_currency = purse.get_currency(shop.currency)
        if total_cost > player_currency:
            print('Insufficient ' + shop.currency + '. Need ' + str(total_cost - player_currency) + ' more.')
            print()
        else:
            items = map(lambda x: loader.load_item(x), item_purchases)
            inventory.add_items(items)
            purse.lose_currency(shop.currency, total_cost)
            print("Items successfully purchased!")
            print()


def shop_sell(item_references):
    shop = __load_current_shop()
    item_sales = []

    for item_reference in item_references:
        item = __get_item_from_sell_list(shop, item_reference)
        if not item:
            __item_not_found(item_reference)
        else:
            item_sales.append(item)

    if len(item_references) != len(item_sales):
        print('The sale will not proceed without all requested items found.')
        print()
    else:
        player_items, items_not_in_inventory = __remove_items_to_sell(inventory.get_inventory_contents(), item_sales)

        if not items_not_in_inventory:
            print('The following items could not be found in your inventory:')
            print_list(__append_count_to_item_list(items_not_in_inventory))
        else:
            total_cost = reduce(lambda item_name: shop.get_item_for_purchase_cost(item_name), item_sales)
            inventory.__save_inventory(player_items)
            purse = loader.load_purse()
            purse.gain_currency(shop.currency, total_cost)

            print("Items sold! You've received " + str(total_cost) + ' ' + shop.currency + '.')


def __remove_items_to_sell(player_inventory, items_to_sell):
    items_not_in_inventory = []
    for item in items_to_sell:
        position = None
        for index in range(player_inventory):
            if player_inventory[index].item.name == item:
                position = index
                break

        if position is not None:
            player_inventory.pop(position)
        else:
            items_not_in_inventory.append(item)

    return player_inventory, items_not_in_inventory


def __load_current_shop():
    return loader.load_shop('Reolas')


def __construct_cost_list(shop, starting_index=0):
    items = shop.get_items_for_sale_list()
    cost_list = []
    index = starting_index
    for item in items:
        index += 1
        cost_list.append(str(index) + '. ' + item + ' (' + str(shop.get_item_for_sale_cost(item)) + ')')
    return cost_list


def __construct_purchase_list(shop, starting_index=0):
    items = shop.get_items_for_purchase_list()
    cost_list = []
    index = starting_index
    for item in items:
        index += 1
        cost_list.append(str(index) + '. ' + item + ' (' + str(shop.get_item_for_purchase_cost(item)) + ')')
    return cost_list


def __append_count_to_item_list(items, starting_index=0):
    counted_item_list = []
    index = starting_index
    for item in items:
        index += 1
        counted_item_list.append(str(index) + '. ' + item.name)
    return counted_item_list


def __item_not_found(item_name):
    if utils.is_int(item_name):
        print('Position ' + str(item_name) + ' out of bounds.')
    else:
        print('Item "' + item_name + '" could not be found.')


def __get_item_from_shop(shop, equipment, item_reference):
    item = __get_item_from_buy_list(shop, item_reference)
    if item is not None:
        return item, 'sales'

    item = __get_item_from_sell_list(shop, item_reference)
    if item is not None:
        return item, 'purchases'

    item = __get_item_from_inventory(shop, equipment, item_reference)
    if item is not None:
        return item, 'equipment'

    return None, None


def __get_item_from_buy_list(shop, item_reference):
    item = None
    sales_list_length = len(shop.get_items_for_sale_list())

    if utils.is_int(item_reference):
        item_reference = int(item_reference) - 1
        if sales_list_length > 0 and 0 <= item_reference < sales_list_length:
            item = shop.get_item_for_sale_at_index(item_reference)
    elif shop.get_item_for_sale_cost(item_reference):
        item = loader.load_item(item_reference)

    return item


def __get_item_from_sell_list(shop, item_reference):
    item = None
    sales_list_length = len(shop.get_items_for_sale_list())
    purchases_list_length = len(shop.get_items_for_purchase_list())
    shop_length = sales_list_length + purchases_list_length

    if utils.is_int(item_reference):
        item_reference = int(item_reference) - 1
        if sales_list_length <= item_reference < shop_length:
            item = shop.get_item_for_purchase_at_index(item_reference - sales_list_length)
    elif shop.get_item_for_purchase_cost(item_reference):
        item = loader.load_item(item_reference)

    return item


def __get_item_from_inventory(shop, equipment, item_reference):
    item = None
    shop_length = len(shop.get_items_for_sale_list()) + len(shop.get_items_for_purchase_list())
    equipment_list_length = len(equipment)

    if utils.is_int(item_reference):
        item_reference = int(item_reference) - 1
        if shop_length <= item_reference < equipment_list_length + shop_length:
            item = equipment[item_reference - shop_length]
    else:
        for inventory_item in equipment:
            if inventory_item.name == item_reference:
                item = inventory_item
                break

    return item
