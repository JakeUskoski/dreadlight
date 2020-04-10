from dreadlight.common.item import Item, ItemType, EquipmentType, EquipmentSubType
from dreadlight.common.stat import Attribute, Stat
from dreadlight.data import store, reset
from dreadlight.player import inventory
from dreadlight.player.purse import Purse


def get_weapons():
    weapons = []

    weapon = Item("Tree Branch", "You have to make do with what nature provides.")
    weapon.add_type(ItemType.EQUIPMENT)
    weapon.set_equipment_type_subtype(EquipmentType.WEAPON, EquipmentSubType.OFFENSIVE)
    weapon.add_attribute(Attribute.ATTACK_DAMAGE, 14)

    weapons.append(weapon)

    weapon = Item("Shank", "Careful! You could stab someone with that.")
    weapon.add_type(ItemType.EQUIPMENT)
    weapon.set_equipment_type_subtype(EquipmentType.WEAPON, EquipmentSubType.OFFENSIVE)
    weapon.add_attribute(Attribute.ATTACK_DAMAGE, 10)
    weapon.add_attribute(Attribute.SKILL_DAMAGE, 25)
    weapon.add_attribute(Attribute.CRITICAL_RATE, 10)
    weapon.add_requirement(Stat.DEXTERITY, 10)

    weapons.append(weapon)

    weapon = Item("Short Sword", "It's a sword.")
    weapon.add_type(ItemType.EQUIPMENT)
    weapon.set_equipment_type_subtype(EquipmentType.WEAPON, EquipmentSubType.OFFENSIVE)
    weapon.add_attribute(Attribute.ATTACK_DAMAGE, 36)
    weapon.add_requirement(Stat.STRENGTH, 10)

    weapons.append(weapon)

    weapon = Item("Large Club", "It gets the job done.")
    weapon.add_type(ItemType.EQUIPMENT)
    weapon.set_equipment_type_subtype(EquipmentType.WEAPON, EquipmentSubType.BOTH)
    weapon.add_attribute(Attribute.ATTACK_DAMAGE, 60)
    weapon.add_requirement(Stat.STRENGTH, 16)

    weapons.append(weapon)

    weapon = Item("Harry's Wand", "You're a wizard.")
    weapon.add_type(ItemType.EQUIPMENT)
    weapon.set_equipment_type_subtype(EquipmentType.WEAPON, EquipmentSubType.SUPPORTIVE)
    weapon.add_attribute(Attribute.MAGIC_DAMAGE, 45)
    weapon.add_requirement(Stat.BLESSINGS, 10)

    weapons.append(weapon)

    weapon = Item("Godslayer", "I mean, it hasn't slain a God--yet.")
    weapon.add_type(ItemType.EQUIPMENT)
    weapon.set_equipment_type_subtype(EquipmentType.WEAPON, EquipmentSubType.BOTH)
    weapon.add_attribute(Attribute.ATTACK_DAMAGE, 30)
    weapon.add_attribute(Attribute.SKILL_DAMAGE, 10)
    weapon.add_attribute(Attribute.CRITICAL_RATE, 5)
    weapon.add_attribute(Attribute.MAGIC_RESISTANCE, 3)
    weapon.add_requirement(Stat.STRENGTH, 18)
    weapon.add_requirement(Stat.DEXTERITY, 14)

    weapons.append(weapon)

    return weapons


def get_shields():
    shields = []

    shield = Item("Wooden Shield", "It's a shield.")
    shield.add_type(ItemType.EQUIPMENT)
    shield.set_equipment_type_subtype(EquipmentType.WEAPON, EquipmentSubType.DEFENSIVE)
    shield.add_attribute(Attribute.ATTACK_RESISTANCE, 2)
    shield.add_attribute(Attribute.SKILL_RESISTANCE, 1)
    shield.add_requirement(Stat.STRENGTH, 7)

    shields.append(shield)

    shield = Item("Kite Shield", "Not meant for flight.")
    shield.add_type(ItemType.EQUIPMENT)
    shield.set_equipment_type_subtype(EquipmentType.WEAPON, EquipmentSubType.DEFENSIVE)
    shield.add_attribute(Attribute.ATTACK_RESISTANCE, 7)
    shield.add_attribute(Attribute.SKILL_RESISTANCE, 14)
    shield.add_attribute(Attribute.MAGIC_RESISTANCE, 9)
    shield.add_requirement(Stat.STRENGTH, 12)

    shields.append(shield)

    return shields


def get_armour():
    armours = []

    armour = Item("Ron's Helmet", 'A good starting Helmet.')
    armour.add_type(ItemType.EQUIPMENT)
    armour.set_equipment_type_subtype(EquipmentType.HEAD, None)
    armour.add_attribute(Attribute.HEALTH, 10)
    armour.add_attribute(Attribute.ATTACK_RESISTANCE, 2)
    armour.add_attribute(Attribute.SKILL_RESISTANCE, 1)
    armour.add_attribute(Attribute.MAGIC_RESISTANCE, 1)
    armour.add_requirement(Stat.STRENGTH, 13)

    armours.append(armour)

    armour = Item("Ron's Chainmail", 'A good starting chest piece.')
    armour.add_type(ItemType.EQUIPMENT)
    armour.set_equipment_type_subtype(EquipmentType.BODY, EquipmentSubType.UPPER)
    armour.add_attribute(Attribute.HEALTH, 50)
    armour.add_attribute(Attribute.ATTACK_RESISTANCE, 6)
    armour.add_attribute(Attribute.SKILL_RESISTANCE, 4)
    armour.add_attribute(Attribute.MAGIC_RESISTANCE, 2)
    armour.add_requirement(Stat.STRENGTH, 14)

    armours.append(armour)

    armour = Item("Ron's Pants", 'A good starting pair of pants.')
    armour.add_type(ItemType.EQUIPMENT)
    armour.set_equipment_type_subtype(EquipmentType.BODY, EquipmentSubType.LOWER)
    armour.add_attribute(Attribute.HEALTH, 20)
    armour.add_attribute(Attribute.ATTACK_RESISTANCE, 3)
    armour.add_attribute(Attribute.SKILL_RESISTANCE, 2)
    armour.add_attribute(Attribute.MAGIC_RESISTANCE, 1)
    armour.add_requirement(Stat.STRENGTH, 14)

    armours.append(armour)

    armour = Item("Ron's Greaves", 'A good starting pair of shoes.')
    armour.add_type(ItemType.EQUIPMENT)
    armour.set_equipment_type_subtype(EquipmentType.FEET, None)
    armour.add_attribute(Attribute.HEALTH, 5)
    armour.add_attribute(Attribute.ATTACK_RESISTANCE, 3)
    armour.add_attribute(Attribute.SKILL_RESISTANCE, 1)
    armour.add_attribute(Attribute.MAGIC_RESISTANCE, 1)
    armour.add_requirement(Stat.STRENGTH, 10)

    armours.append(armour)

    armour = Item("Cloth Shirt", 'The stains add character.')
    armour.add_type(ItemType.EQUIPMENT)
    armour.set_equipment_type_subtype(EquipmentType.BODY, EquipmentSubType.UPPER)
    armour.add_attribute(Attribute.HEALTH, 20)
    armour.add_attribute(Attribute.ATTACK_RESISTANCE, 3)
    armour.add_attribute(Attribute.SKILL_RESISTANCE, 2)
    armour.add_attribute(Attribute.MAGIC_RESISTANCE, 1)

    armours.append(armour)

    armour = Item("Cloth Pants", 'A little breezy.')
    armour.add_type(ItemType.EQUIPMENT)
    armour.set_equipment_type_subtype(EquipmentType.BODY, EquipmentSubType.LOWER)
    armour.add_attribute(Attribute.HEALTH, 10)
    armour.add_attribute(Attribute.ATTACK_RESISTANCE, 1)

    armour = Item("Cloth Boots", 'Better than nothing.')
    armour.add_type(ItemType.EQUIPMENT)
    armour.set_equipment_type_subtype(EquipmentType.FEET, None)
    armour.add_attribute(Attribute.HEALTH, 5)
    armour.add_attribute(Attribute.DODGE_RATE, 1)

    armours.append(armour)

    armour = Item("Dirk's Armour", 'Sharpest plate mail in the land.')
    armour.add_type(ItemType.EQUIPMENT)
    armour.set_equipment_type_subtype(EquipmentType.BODY, EquipmentSubType.BOTH)
    armour.add_attribute(Attribute.HEALTH, 110)
    armour.add_attribute(Attribute.ATTACK_DAMAGE, 5)
    armour.add_attribute(Attribute.SKILL_DAMAGE, 5)
    armour.add_attribute(Attribute.ATTACK_RESISTANCE, 40)
    armour.add_attribute(Attribute.SKILL_RESISTANCE, 18)
    armour.add_attribute(Attribute.MAGIC_RESISTANCE, 14)
    armour.add_requirement(Stat.STRENGTH, 18)
    armour.add_requirement(Stat.DEXTERITY, 20)
    armour.add_requirement(Stat.CONSTITUTION, 24)

    armours.append(armour)

    return armours


def get_accessories():
    accessories = []

    accessory = Item("Opal Necklace", 'Quite the jewel.')
    accessory.add_type(ItemType.EQUIPMENT)
    accessory.add_type(ItemType.PRECIOUS)
    accessory.set_equipment_type_subtype(EquipmentType.NECKLACE, EquipmentSubType.ACCESSORY)
    accessory.add_attribute(Attribute.MANA, 10)
    accessory.add_attribute(Attribute.MAGIC_DAMAGE, 10)

    accessories.append(accessory)

    accessory = Item("Bronze Chain", "It's getting pretty rusty these days.")
    accessory.add_type(ItemType.EQUIPMENT)
    accessory.set_equipment_type_subtype(EquipmentType.NECKLACE, EquipmentSubType.ACCESSORY)
    accessory.add_attribute(Attribute.CRITICAL_RATE, 5)

    accessories.append(accessory)

    accessory = Item("Plain Ring", "Simplicity is elegance.")
    accessory.add_type(ItemType.EQUIPMENT)
    accessory.add_type(ItemType.PRECIOUS)
    accessory.set_equipment_type_subtype(EquipmentType.RING, EquipmentSubType.ACCESSORY)
    accessory.add_attribute(Attribute.STAMINA, 5)

    accessories.append(accessory)

    accessory = Item("Plain Earring", "Simplicity is elegance.")
    accessory.add_type(ItemType.EQUIPMENT)
    accessory.add_type(ItemType.PRECIOUS)
    accessory.set_equipment_type_subtype(EquipmentType.RING, EquipmentSubType.ACCESSORY)
    accessory.add_attribute(Attribute.EXP_RATE, 2)

    accessories.append(accessory)

    return accessories


def reset_all():
    reset.items()
    reset.inventory()
    reset.purse()


def initialize():
    all_items = []
    all_items.extend(get_weapons())
    all_items.extend(get_shields())
    all_items.extend(get_armour())
    all_items.extend(get_accessories())
    for item in all_items:
        store.store_item(item)
    inventory.add_items(get_armour())
    some_purse = Purse()
    some_purse.gain_currency('Shuckles', 300)
