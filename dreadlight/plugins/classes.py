from dreadlight.common.playable_class import PlayableClass
from dreadlight.common.stat import Stat
from dreadlight.data import store, reset


def get_classes():
    playable_classes = []

    playable_class = PlayableClass("Knight", "All life needs is a well-balanced blade.")
    playable_class.add_stat(Stat.STRENGTH, 14)
    playable_class.add_stat(Stat.DEXTERITY, 12)
    playable_class.add_stat(Stat.WILL, 8)
    playable_class.add_stat(Stat.BLESSINGS, 4)
    playable_class.add_stat(Stat.CONSTITUTION, 13)
    playable_class.add_stat(Stat.INGENUITY, 11)
    playable_class.add_stat(Stat.LUCK, 7)
    playable_class.add_equipment("Ron's Helmet")
    playable_class.add_equipment("Ron's Chainmail")
    playable_class.add_equipment("Ron's Pants")
    playable_class.add_equipment("Ron's Greaves")
    playable_class.add_equipment("Short Sword")
    playable_class.add_equipment("Kite Shield")

    playable_classes.append(playable_class)

    playable_class = PlayableClass("Guardian", "Too many journeys are snuffed out by weakness.")
    playable_class.add_stat(Stat.STRENGTH, 12)
    playable_class.add_stat(Stat.DEXTERITY, 4)
    playable_class.add_stat(Stat.WILL, 6)
    playable_class.add_stat(Stat.BLESSINGS, 14)
    playable_class.add_stat(Stat.CONSTITUTION, 17)
    playable_class.add_stat(Stat.INGENUITY, 10)
    playable_class.add_stat(Stat.LUCK, 5)
    playable_class.add_equipment("Cloth Shirt")
    playable_class.add_equipment("Cloth Pants")
    playable_class.add_equipment("Ron's Greaves")
    playable_class.add_equipment("Short Sword")
    playable_class.add_equipment("Kite Shield")
    playable_class.add_equipment("Opal Necklace")

    playable_classes.append(playable_class)

    playable_class = PlayableClass("Quickfoot", "I'll be done before you're done asking where I've gone.")
    playable_class.add_stat(Stat.STRENGTH, 8)
    playable_class.add_stat(Stat.DEXTERITY, 17)
    playable_class.add_stat(Stat.WILL, 12)
    playable_class.add_stat(Stat.BLESSINGS, 3)
    playable_class.add_stat(Stat.CONSTITUTION, 7)
    playable_class.add_stat(Stat.INGENUITY, 10)
    playable_class.add_stat(Stat.LUCK, 12)
    playable_class.add_equipment("Cloth Shirt")
    playable_class.add_equipment("Cloth Pants")
    playable_class.add_equipment("Cloth Shoes")
    playable_class.add_equipment("Shank")
    playable_class.add_equipment("Wooden Shield")
    playable_class.add_equipment("Plain Ring")

    playable_classes.append(playable_class)

    playable_class = PlayableClass("Gambler", "Something tells me I'll pick the right card.")
    playable_class.add_stat(Stat.STRENGTH, 6)
    playable_class.add_stat(Stat.DEXTERITY, 15)
    playable_class.add_stat(Stat.WILL, 9)
    playable_class.add_stat(Stat.BLESSINGS, 3)
    playable_class.add_stat(Stat.CONSTITUTION, 7)
    playable_class.add_stat(Stat.INGENUITY, 16)
    playable_class.add_stat(Stat.LUCK, 17)
    playable_class.add_equipment("Cloth Shirt")
    playable_class.add_equipment("Cloth Pants")
    playable_class.add_equipment("Cloth Shoes")
    playable_class.add_equipment("Shank")
    playable_class.add_equipment("Plain Ring")
    playable_class.add_equipment("Plain Ring")
    playable_class.add_equipment("Bronze Chain")
    playable_class.add_equipment("Plain Earring")
    playable_class.add_equipment("Plain Earring")

    playable_classes.append(playable_class)

    playable_class = PlayableClass("Witch", "Swords are overrated. Magic is law now.")
    playable_class.add_stat(Stat.STRENGTH, 3)
    playable_class.add_stat(Stat.DEXTERITY, 3)
    playable_class.add_stat(Stat.WILL, 19)
    playable_class.add_stat(Stat.BLESSINGS, 16)
    playable_class.add_stat(Stat.CONSTITUTION, 6)
    playable_class.add_stat(Stat.INGENUITY, 16)
    playable_class.add_stat(Stat.LUCK, 6)
    playable_class.add_equipment("Cloth Shirt")
    playable_class.add_equipment("Cloth Pants")
    playable_class.add_equipment("Cloth Shoes")
    playable_class.add_equipment("Tree Branch")
    playable_class.add_equipment("Harry's Wand")
    playable_class.add_equipment("Opal Necklace")
    playable_class.add_equipment("Plain Earring")
    playable_class.add_equipment("Plain Earring")

    playable_classes.append(playable_class)

    playable_class = PlayableClass("Apothecary", "A helping hand, a helping fist.")
    playable_class.add_stat(Stat.STRENGTH, 11)
    playable_class.add_stat(Stat.DEXTERITY, 3)
    playable_class.add_stat(Stat.WILL, 14)
    playable_class.add_stat(Stat.BLESSINGS, 13)
    playable_class.add_stat(Stat.CONSTITUTION, 12)
    playable_class.add_stat(Stat.INGENUITY, 8)
    playable_class.add_stat(Stat.LUCK, 8)
    playable_class.add_equipment("Cloth Shirt")
    playable_class.add_equipment("Cloth Pants")
    playable_class.add_equipment("Ron's Greaves")
    playable_class.add_equipment("Short Sword")
    playable_class.add_equipment("Harry's Wand")
    playable_class.add_equipment("Opal Necklace")
    playable_class.add_equipment("Plain Ring")
    playable_class.add_equipment("Plain Earring")

    playable_classes.append(playable_class)

    playable_class = PlayableClass("Goliath", "The largest survive.")
    playable_class.add_stat(Stat.STRENGTH, 17)
    playable_class.add_stat(Stat.DEXTERITY, 4)
    playable_class.add_stat(Stat.WILL, 15)
    playable_class.add_stat(Stat.BLESSINGS, 5)
    playable_class.add_stat(Stat.CONSTITUTION, 17)
    playable_class.add_stat(Stat.INGENUITY, 6)
    playable_class.add_stat(Stat.LUCK, 5)
    playable_class.add_equipment("Ron's Helmet")
    playable_class.add_equipment("Ron's Chainmail")
    playable_class.add_equipment("Ron's Pants")
    playable_class.add_equipment("Ron's Greaves")
    playable_class.add_equipment("Large Club")
    playable_class.add_equipment("Bronze Chain")

    playable_classes.append(playable_class)

    return playable_classes


def reset_all():
    reset.classes()


def initialize():
    for __class in get_classes():
        store.store_class(__class)
