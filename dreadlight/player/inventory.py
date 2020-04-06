from dreadlight.common import utils
from dreadlight.common.item import InventoryItem, EquipmentType, EquipmentSubType
from dreadlight.data import store, loader


def __get_item_name(inventory_item):
    return inventory_item.item.name


def __load_inventory():
    items = loader.load_inventory()
    if items:
        items.sort(key=__get_item_name)
    return items


def __add_item_to_inventory(inventory, item):
    inventory.append(InventoryItem(item, False))


def __save_inventory(inventory):
    store.store_inventory(inventory)


def __remove_position_from_inventory(position):
    inventory = __load_inventory()
    translated_position = int(position) - 1
    if 0 <= translated_position < len(inventory):
        item = inventory.pop(int(position))
        __save_inventory(inventory)
        return item
    return None


def __remove_item_from_inventory(item_name):
    inventory = __load_inventory()
    for item in inventory:
        if utils.caseless_equal(item.item.name, item_name):
            inventory.remove(item)
            __save_inventory(inventory)
            return item
    return None


def __get_item_from_inventory_via_position(position):
    inventory = __load_inventory()
    translated_position = int(position) - 1
    if 0 <= translated_position < len(inventory):
        return inventory[translated_position]
    return None


def __get_item_from_inventory_via_name(name):
    for inventory_item in __load_inventory():
        if utils.caseless_equal(name, inventory_item.item.name):
            return inventory_item
    return None


def __remove_items(item_names_or_positions):
    item_refs = []
    position_refs = []
    removals = []
    failures = []
    inventory = __load_inventory()
    inventory_length = len(inventory)

    for ref in item_names_or_positions:
        if utils.is_int(ref):
            translated_position = int(ref) - 1
            if 0 <= translated_position < inventory_length:
                position_refs.append(translated_position)
            else:
                failures.append(ref)
        else:
            item_refs.append(ref)

    for index, item in enumerate(inventory):
        for item_ref in item_refs:
            if utils.caseless_equal(item_ref, item.item.name) and \
                    not item.is_equipped:
                position_refs.append(index)
                item_refs.remove(item_ref)
                break

    failures.extend(item_refs)

    position_refs.sort(reverse=True)
    for position in position_refs:
        removals.append(inventory.pop(position).item)

    __save_inventory(inventory)

    return removals, failures


def __get_equipped_of_type(equipment_type, subset):
    already_equipped = []
    equipped_subtypes = []
    for equipped_item in subset:
        if equipped_item.equipment_type == equipment_type:
            already_equipped.append(equipped_item)
            equipped_subtypes.append(equipped_item.equipment_subtype)
    return already_equipped, equipped_subtypes


def __check_equipped_weapons_body(item, subset):
    already_equipped, equipped_subtypes = __get_equipped_of_type(item.equipment_type, subset)
    equip_count = len(already_equipped)

    if equip_count > 0:
        if (EquipmentSubType.BOTH in equipped_subtypes or
                EquipmentSubType.BOTH == item.equipment_subtype):
            return already_equipped

        for equipped in already_equipped:
            if item.equipment_subtype == equipped.equipment_subtype:
                return [equipped]

        if equip_count == 2:
            return already_equipped

    return None


def __check_equipped_earrings_rings(item, subset):
    already_equipped, equipped_subtypes = __get_equipped_of_type(item.equipment_type, subset)
    equip_count = len(already_equipped)

    if (equip_count == 2 or
            (equip_count == 1 and
             (EquipmentSubType.BOTH in equipped_subtypes or
              EquipmentSubType.BOTH == item.equipment_subtype))):
        return already_equipped

    return None


def __check_equipped_head_necklace_feet(item, subset):
    already_equipped, equipped_subtypes = __get_equipped_of_type(item.equipment_type, subset)

    if len(already_equipped) != 0:
        return already_equipped
    else:
        return None


def __can_equip_item(item, subset):
    if EquipmentType.WEAPON == item.equipment_type or \
            EquipmentType.BODY == item.equipment_type:
        return __check_equipped_weapons_body(item, subset)
    elif EquipmentType.EARRING == item.equipment_type or \
            EquipmentType.RING == item.equipment_type:
        return __check_equipped_earrings_rings(item, subset)
    else:
        return __check_equipped_head_necklace_feet(item, subset)


##########################
#       PUBLIC API       #
##########################


def get_inventory_list():
    items = []
    counter = 1
    for inventory_item in __load_inventory():
        string = str(counter) + '. ' + inventory_item.item.name
        if inventory_item.is_equipped:
            string += ' (e)'
        items.append(string)
        counter += 1
    return items


def get_inventory_contents():
    return __load_inventory()


def get_equipment():
    items = []
    for item in __load_inventory():
        if item.is_equipped:
            items.append(item)
    return items


def get_details_of_item(item_name_or_position):
    if utils.is_int(item_name_or_position):
        return __get_item_from_inventory_via_position(item_name_or_position)
    else:
        return __get_item_from_inventory_via_name(item_name_or_position)


def toss_items(item_names_or_positions):
    removals, failures = __remove_items(item_names_or_positions)
    removed_item_names = map(lambda item: item.name, removals)
    return removed_item_names, failures


def add_item(item):
    add_items([item])


def add_items(items):
    inventory = __load_inventory()
    for item in items:
        __add_item_to_inventory(inventory, item)
    __save_inventory(inventory)


def equip_item(item_name_or_position):
    items = __load_inventory()
    equipped_items = list(map(lambda item: item.item, [item for item in items if item.is_equipped]))
    item = None

    if utils.is_int(item_name_or_position):
        translated_position = int(item_name_or_position) - 1
        if 0 <= translated_position < len(items):
            item = items[int(translated_position)]
    else:
        for inventory_item in items:
            if utils.caseless_equal(inventory_item.item.name, item_name_or_position):
                item = inventory_item
                break

    if item is None:
        return []

    if item.item in equipped_items:
        return ['']

    already_equipped = __can_equip_item(item.item, equipped_items)
    if already_equipped is None:
        item.equip()
        __save_inventory(items)
        return None
    else:
        return already_equipped


def unequip_item(item_name_or_position):
    items = __load_inventory()

    if utils.is_int(item_name_or_position):
        translated_position = int(item_name_or_position) - 1
        if 0 <= translated_position < len(items) and \
                items[int(translated_position)].is_equipped:
            items[int(translated_position)].unequip()
            __save_inventory(items)
            return True
    else:
        for item in items:
            if utils.caseless_equal(item.item.name, item_name_or_position) and \
                    item.is_equipped:
                item.unequip()
                __save_inventory(items)
                return True
    return False
