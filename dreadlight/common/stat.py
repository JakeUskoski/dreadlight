from enum import Enum, unique


@unique
class Type(Enum):
    RESOURCE = 'resource',
    DAMAGE = 'damage',
    RESISTANCE = 'resistance',
    GROWTH = 'growth'

    def get_name(self):
        return str(self)[5:].replace('_', ' ').title()


@unique
class Concept(Enum):
    PHYSICAL = 'physical',
    SKILLFUL = 'skillful',
    MAGICAL = 'magical',
    GLOBAL = 'global'

    def get_name(self):
        return str(self)[8:].replace('_', ' ').title()


@unique
class Attribute(Enum):
    HEALTH = {'type': Type.RESOURCE, 'concept': Concept.PHYSICAL},
    STAMINA = {'type': Type.RESOURCE, 'concept': Concept.SKILLFUL},
    MANA = {'type': Type.RESOURCE, 'concept': Concept.MAGICAL},
    ABILITY_SLOTS = {'type': Type.RESOURCE, 'concept': Concept.GLOBAL},
    ATTACK_DAMAGE = {'type': Type.DAMAGE, 'concept': Concept.PHYSICAL},
    SKILL_DAMAGE = {'type': Type.DAMAGE, 'concept': Concept.SKILLFUL},
    MAGIC_DAMAGE = {'type': Type.DAMAGE, 'concept': Concept.MAGICAL},
    CRITICAL_RATE = {'type': Type.DAMAGE, 'concept': Concept.GLOBAL},
    ATTACK_RESISTANCE = {'type': Type.RESISTANCE, 'concept': Concept.PHYSICAL},
    SKILL_RESISTANCE = {'type': Type.RESISTANCE, 'concept': Concept.SKILLFUL},
    MAGIC_RESISTANCE = {'type': Type.RESISTANCE, 'concept': Concept.MAGICAL},
    DODGE_RATE = {'type': Type.RESISTANCE, 'concept': Concept.GLOBAL},
    ITEM_RATE = {'type': Type.GROWTH, 'concept': Concept.PHYSICAL},
    UPGRADE_RATE = {'type': Type.GROWTH, 'concept': Concept.SKILLFUL},
    GOLD_RATE = {'type': Type.GROWTH, 'concept': Concept.MAGICAL},
    EXP_RATE = {'type': Type.GROWTH, 'concept': Concept.GLOBAL}

    def get_name(self):
        return str(self)[10:].replace('_', ' ').title()


@unique
class Stat(Enum):
    STRENGTH = [Attribute.ATTACK_DAMAGE, Attribute.MAGIC_RESISTANCE],
    DEXTERITY = [Attribute.SKILL_DAMAGE, Attribute.DODGE_RATE],
    WILL = [Attribute.MAGIC_DAMAGE, Attribute.STAMINA],
    BLESSINGS = [Attribute.MANA, Attribute.SKILL_RESISTANCE, Attribute.GOLD_RATE],
    CONSTITUTION = [Attribute.HEALTH, Attribute.ATTACK_RESISTANCE],
    INGENUITY = [Attribute.ABILITY_SLOTS, Attribute.EXP_RATE, Attribute.UPGRADE_RATE],
    LUCK = [Attribute.ITEM_RATE, Attribute.CRITICAL_RATE]

    def get_name(self):
        return str(self)[5:].replace('_', ' ').title()


class Stats:
    def __init__(self):
        self.dictionary = {}

    @staticmethod
    def load_stats(stat_dictionary):
        stats = Stats()
        for stat in stat_dictionary:
            stat_name = str(stat['stat'])
            stats.set_stat(Stat[stat_name[5:]], stat['value'])
        return stats

    def get_stat(self, stat):
        if str(stat) not in self.dictionary:
            return None
        return self.dictionary[str(stat)]

    def set_stat(self, stat, value):
        self.dictionary[str(stat)] = value

    def get_stats_dictionary(self):
        return self.dictionary

    def __str__(self):
        return_string = '['
        for stat in Stat:
            if self.get_stat(stat) is not None:
                return_string += '{"stat":"' + str(stat) + '",' + \
                                 '"value":' + str(self.get_stat(stat)) + '},'
        if return_string != '[':
            return_string = return_string[0:-1]
        return return_string + ']'

    @staticmethod
    def add_stats_together(stats, other_stats):
        new_stats = Stats()

        for stat in Stat:
            total_value = 0
            value = stats.get_stat(stat)
            other_value = other_stats.get_stat(stat)

            if value is not None:
                total_value += value

            if other_value is not None:
                total_value += other_value

            if new_stats != 0:
                new_stats.set_stat(stat, total_value)

        return new_stats

    @staticmethod
    def compare_stats(stats, other_stats):
        stats_difference = Stats()
        for stat in Stat:
            total_value = None
            value = stats.get_stat(stat)
            other_value = other_stats.get_stat(stat)

            if value is not None:
                total_value = value

            if other_value is not None:
                if total_value is None:
                    total_value = 0
                total_value -= other_value

            stats_difference.set_stat(stat, total_value)
        return stats_difference


class Attributes:
    def __init__(self):
        self.dictionary = {}

    @staticmethod
    def load_attributes(attribute_dictionary):
        attributes = Attributes()
        for attribute in attribute_dictionary:
            attribute_name = str(attribute['attribute'])
            attributes.set_attribute(Attribute[attribute_name[10:]], attribute['value'])
        return attributes

    def get_attribute(self, attribute):
        if str(attribute) not in self.dictionary:
            return None
        return self.dictionary[str(attribute)]

    def set_attribute(self, attribute, value):
        self.dictionary[str(attribute)] = value

    def get_attribute_dictionary(self):
        return self.dictionary

    def __str__(self):
        return_string = '['
        for attribute in Attribute:
            if self.get_attribute(attribute) is not None:
                return_string += '{"attribute":"' + str(attribute) + '",' + \
                                 '"value":' + str(self.get_attribute(attribute)) + '},'
        if return_string != '[':
            return_string = return_string[0:-1]
        return return_string + ']'

    @staticmethod
    def add_attributes_together(attributes, other_attributes):
        new_attributes = Attributes()

        for attribute in Attribute:
            total_value = 0
            value = attributes.get_attribute(attribute)
            other_value = other_attributes.get_attribute(attribute)

            if value is not None:
                total_value += value

            if other_value is not None:
                total_value += other_value

            if total_value != 0:
                new_attributes.set_attribute(attribute, total_value)

        return new_attributes

    @staticmethod
    def compare_attributes(attributes, other_attributes):
        attributes_difference = Attributes()

        for attribute in Attribute:
            total_value = None
            value = attributes.get_attribute(attribute)
            other_value = other_attributes.get_attribute(attribute)

            if value is not None:
                total_value = value

            if other_value is not None:
                if total_value is None:
                    total_value = 0
                total_value -= other_value

            attributes_difference.set_attribute(attribute, total_value)

        return attributes_difference
