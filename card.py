class Card:

    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

    def __repr__(self):
        return self.name + "," + self.color + "," + self.type

    def __eq__(self,other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(str(self.name) + str(self.color) + str(self.type))