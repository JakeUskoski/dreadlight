from dreadlight.common.stat import Stats


class PlayableClass:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.stats = Stats()
        self.starting_equipment = []

    @staticmethod
    def load_class(class_dict):
        new_class = PlayableClass(class_dict['name'], class_dict['description'])
        new_class.stats = Stats.load_stats(class_dict['stats'])
        new_class.starting_equipment = class_dict['starting_equipment']

    def add_stat(self, stat, value):
        self.stats.set_stat(stat, value)

    def add_equipment(self, item_name):
        return self.starting_equipment.append(item_name)

    def __str__(self):
        string = '{"name":"' + self.name + '"' + \
                 ',"description":"' + self.description + '"' + \
                 ',"stats":' + str(self.stats) + \
                 ',"starting_equipment":['

        if self.starting_equipment:
            for item_name in self.starting_equipment:
                string += '"' + item_name + '",'
            string = string[0:-1]
        string += ']}'

        return string
