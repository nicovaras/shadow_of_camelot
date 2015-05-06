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
        pass

    def get_all_three_equal_cards(self):
        count = {}
        for c in self.cards:
          if c not in count.keys():
            count[c] = 0
          count[c] += 1
        return [c for c in count.keys() if count[c] >= 3]

    def choose_and_discard_three(self, card_groups):
        chosen_card = self.choose_one_from(card_groups)
        for i in range(3):
            index = self.cards.index(chosen_card)
            self.cards = self.cards[:index] + self.cards[index+1:]

    def choose_one_from(self, card_groups):
        #TODO: placeholder
        return card_groups[0]