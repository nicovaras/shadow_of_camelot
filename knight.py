import random
from constants import *

class Knight:

    def __init__(self, name):
        self.name = name
        self.life = 4
        self.relic = None
        self.special_power = None
        self.cards = []

    def choose_evil_action(self):
        actions = [BLACK_CARD_ACTION, 
                   SIEGE_ACTION, 
                   LOSE_LIFE_ACTION]
        return random.choice(actions)

    def choose_heroic_action(self):
        actions = [MOVE_ACTION, 
                   CURRENT_QUEST_ACTION, 
                   SPECIAL_CARD_ACTION,
                   HEAL_ACTION]
        return random.choice(actions)

    def choose_new_location(self, current_positions):
        assert False