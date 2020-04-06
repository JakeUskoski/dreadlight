from enum import Enum, unique

from dreadlight.common import utils
from dreadlight.common.stat import Attributes, Stats


@unique
class ItemType(Enum):
    EQUIPMENT = 'Equipment',
    CONSUMABLE = 'Consumable',
    CRAFTING = 'Crafting Supply',
    PRECIOUS = 'Precious',
    QUEST = 'Quest Item'

    def get_name(self):
        return str(self)[9:].replace('_', ' ').title()


@unique
class EquipmentType(Enum):
    HEAD = 'Head',
    EARRING = 'Earring',
    NECKLACE = 'Necklace',
    RING = 'Ring',
    BODY = 'Body',
    FEET = 'Feet',
    WEAPON = 'Weapon'

    def get_name(self):
        return str(self)[14:].replace('_', ' ').title()


@unique
class EquipmentSubType(Enum):
    UPPER = 'Upper',
    LOWER = 'Lower',
    BOTH = 'Both',
    CATALYST = 'Catalyst',
    AMMO = 'Ammunition',
    ACCESSORY = 'Accessory',
    OFFENSIVE = 'Offensive',
    DEFENSIVE = 'Defensive',
    SUPPORTIVE = 'Supportive'

    def get_name(self):
        return str(self)[17:].replace('_', ' ').title()


class InventoryItem:
    def __init__(self, item, is_equipped):
        self.item = item
        self.is_equipped = is_equipped

    @staticmethod
    def load_item(item_dictionary):
        return InventoryItem(Item.load_item(item_dictionary['item']), item_dictionary['is_equipped'])

    def equip(self):
        self.is_equipped = True

    def unequip(self):
        self.is_equipped = False

    def __str__(self):
        return '{"item":' + str(self.item) + \
               ',"is_equipped":' + utils.jsonify_boolean(self.is_equipped) + '}'


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.attributes = Attributes()
        self.requirements = Stats()
        self.item_types = []
        self.equipment_type = None
        self.equipment_subtype = None

    @staticmethod
    def load_item(item_dictionary):
        new_item = Item(item_dictionary['name'], item_dictionary['description'])
        new_item.attributes = Attributes.load_attributes(item_dictionary['attributes'])
        new_item.requirements = Stats.load_stats(item_dictionary['requirements'])
        for item_type in item_dictionary['item_types']:
            new_item.add_type(ItemType[item_type[9:]])
        if 'equipment_type' in item_dictionary:
            new_item.equipment_type = EquipmentType[item_dictionary['equipment_type'][14:]]
        if 'equipment_subtype' in item_dictionary:
            new_item.equipment_subtype = EquipmentSubType[item_dictionary['equipment_subtype'][17:]]
        return new_item

    def add_type(self, item_type):
        if item_type not in self.item_types:
            self.item_types.append(item_type)

    def set_equipment_type_subtype(self, equipment_type, equipment_subtype):
        self.equipment_type = equipment_type
        self.equipment_subtype = equipment_subtype

    def add_attribute(self, attribute, value):
        self.attributes.set_attribute(attribute, value)

    def add_requirement(self, stat, value):
        self.requirements.set_stat(stat, value)

    def __str__(self):
        string = '{"name":"' + self.name + '"' + \
                 ',"description":"' + self.description + '"' + \
                 ',"attributes":' + str(self.attributes) + \
                 ',"requirements":' + str(self.requirements)
        string += ',"item_types":['
        for item_type in self.item_types:
            string += '"' + str(item_type) + '",'
        string = string[0:-1] + ']'
        if self.equipment_type is not None:
            string += ',"equipment_type":"' + str(self.equipment_type) + '"'
        if self.equipment_subtype is not None:
            string += ',"equipment_subtype":"' + str(self.equipment_subtype) + '"'
        return string + '}'
