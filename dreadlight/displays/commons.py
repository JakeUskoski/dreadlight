import shutil
import sys

######################################
#     DISPLAY ASSISTANCE METHODS     #
######################################
from dreadlight.common.item import InventoryItem, Item
from dreadlight.common.stat import Attribute, Stat, Attributes, Stats
from dreadlight.data import loader

LINE_BREAK = '- - - - -'


def print_item_types(item):
    item_types = ''
    for item_type in item.item_types:
        item_types += item_type.get_name() + ', '
    print('Item Types: ' + item_types[0:-2])
    if item.equipment_type is not None:
        print('Equipment Type: ' + item.equipment_type.get_name())
    if item.equipment_subtype is not None:
        print('Equipment Subtype: ' + item.equipment_subtype.get_name())


def print_stats_attributes_difference(entity, main_value, difference_value):
    if difference_value is not None:
        output = entity.get_name() + ': ' + str(main_value)
        if difference_value > 0:
            output += ' ↑ (+' + str(difference_value) + ')'
        elif difference_value < 0:
            output += ' ↓ (' + str(difference_value) + ')'
        else:
            output += ' (-)'
        print(output)


def print_purse(purse):
    currency_list = purse.get_held_currencies()
    if len(currency_list) == 0:
        print("You don't have any money...")
    else:
        for currency in currency_list:
            print(currency + ': ' + str(purse.get_currency(currency)))


def print_list(input_list):
    (term_width, term_height) = shutil.get_terminal_size()

    repr_list = [str(x) for x in input_list]
    min_chars_between = 3
    usable_term_width = term_width - 1
    min_element_width = min(len(x) for x in repr_list) + min_chars_between
    max_element_width = max(len(x) for x in repr_list) + min_chars_between
    if max_element_width >= usable_term_width:
        ncol = 1
        col_widths = [1]
    else:
        # Start with max possible number of columns and reduce until it fits
        ncol = int(min(len(repr_list), usable_term_width / min_element_width))
        while True:
            col_widths = [max(len(x) + min_chars_between \
                              for j, x in enumerate(repr_list) if j % ncol == i) \
                          for i in range(ncol)]
            if sum(col_widths) <= usable_term_width:
                break
            else:
                ncol -= 1

    for i, x in enumerate(repr_list):
        sys.stdout.write(x.ljust(col_widths[i % ncol]))
        if i == len(repr_list) - 1 or (i + 1) % ncol == 0:
            sys.stdout.write('\n')


def print_item_details(inventory_item):
    item = None
    if type(inventory_item) is type(InventoryItem):
        item = inventory_item.item
    elif type(inventory_item) is type(Item):
        item = inventory_item
    elif type(inventory_item) is type(str):
        item = loader.load_item(inventory_item)
    print()
    print('DETAILS')
    print(LINE_BREAK)
    name = item.name
    if type(inventory_item) is type(InventoryItem) and inventory_item.is_equipped:
        name += ' (equipped)'
    print('Name: ' + name)
    print('Description: ' + item.description)
    print_item_types(item)
    print()
    print('ATTRIBUTES')
    print(LINE_BREAK)
    for attribute in Attribute:
        value = item.attributes.get_attribute(attribute)
        if value is not None:
            print(attribute.get_name() + ': ' + str(value))
    print()
    print('REQUIREMENTS')
    print(LINE_BREAK)
    for stat in Stat:
        value = item.requirements.get_stat(stat)
        if value is not None:
            print(stat.get_name() + ': ' + str(value))
    print()


def print_item_comparison(item, compared_item, item_equipped=False, compared_item_equipped=False):
    if item_equipped or type(item) is type(InventoryItem):
        item = item.item
    if compared_item_equipped or type(compared_item) is type(InventoryItem):
        compared_item = compared_item.item

    compared_attributes = Attributes.compare_attributes(item.attributes, compared_item.attributes)
    compared_requirements = Stats.compare_stats(item.requirements, compared_item.requirements)

    print()
    print('DETAILS')
    print(LINE_BREAK)
    item_name = item.name
    if item_equipped:
        item_name += ' (equipped)'
    print('Item: ' + item_name)
    print_item_types(item)
    print()
    compared_item_name = compared_item.name
    if compared_item_equipped:
        compared_item_name += ' (equipped)'
    print('Compared to: ' + compared_item_name)
    print_item_types(compared_item)
    print()
    print('ATTRIBUTES')
    print(LINE_BREAK)
    for attribute in Attribute:
        item_value = item.attributes.get_attribute(attribute)
        difference_value = compared_attributes.get_attribute(attribute)
        print_stats_attributes_difference(attribute, item_value, difference_value)
    print()
    print('REQUIREMENTS')
    print(LINE_BREAK)
    for stat in Stat:
        item_value = item.requirements.get_stat(stat)
        difference_value = compared_requirements.get_stat(stat)
        print_stats_attributes_difference(stat, item_value, difference_value)
    print()
