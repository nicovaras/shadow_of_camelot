class Card:

    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

    def __repr__(self):
        return self.name + "," + self.color + "," + self.type