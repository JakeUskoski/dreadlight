from dreadlight.common.stat import Stats


class Character:
    def __init__(self, name):
        self.name = name
        self.class_name = ""
        self.stats = Stats()
        self.gold = 0

    def set_class(self, playable_class):
        self.class_name = playable_class.name
        self.stats = playable_class.stats

    @staticmethod
    def load_character(character_dict):
        character = Character(character_dict['name'])
        character.class_name = character_dict['class_name']
        character.stats = Stats.load_stats(character_dict['stats'])
        character.gold = character_dict['gold']
        return character

    def __str__(self):
        return '{"name":"' + self.name + '"' + \
               ',"class_name":"' + self.class_name + '"' + \
               ',"stats":' + str(self.stats) + \
               ',"gold":' + str(self.gold) + '}'
