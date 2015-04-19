import random
from gameboard import Gameboard 
from knight import Knight
from constants import *
from deck import Deck
from knight_factory import KnightFactory

class Relic:
    def __init__(self):
        self.power = None

class Armor(Relic):
    pass


class HolyGrail(Relic):
    pass


class Excalibur(Relic):
    pass


class Game:

    def __init__(self, gameboard, num_players):
        self.gameboard = gameboard
        self.knights = self.init_knights(num_players)
        self.deck = Deck()
        self.current_turn = 0

    def init_knights(self, num_players):
        available_knights = [KnightFactory.Arthur(), KnightFactory.Gawain(),
                             KnightFactory.Galahad(), KnightFactory.Kay(),
                             KnightFactory.Palamedes(),
                             KnightFactory.Percival(), KnightFactory.Tristan()]
        knights = random.sample(available_knights, num_players)
        for knight in knights:
            self.gameboard.move(knight, ROUNDTABLE)
        return knights

    def is_ended(self):
        return self.is_lost() or self.gameboard.round_table.is_full()

    def is_lost(self):
        return (self.gameboard.sieges >= 12 or
                self.gameboard.has_black_sword_majority() or
                self.all_players_died())

    def all_players_died(self):
        for knight in self.knights:
            if knight.life > 0:
                return False
        return True

    def start_game(self):
        for knight in self.knights:
            knight.cards.append(self.deck.pick_card_with('merlin', 'white'))
            for _ in range(5):
                knight.cards.append(self.deck.pick_next('white'))

    def play(self):
        self.start_game()
        while True:
            current_knight = self.next_knight_turn()
            self.progression_of_evil_phase(current_knight)
            if self.is_ended():
                break
            
            self.heroic_action_phase(current_knight)
            if self.is_ended():
                break

    def next_knight_turn(self):
        next = self.knights[self.current_turn]
        self.current_turn = (self.current_turn + 1) % len(self.knights)
        return next


    def progression_of_evil_phase(self, knight):
        action = knight.choose_evil_action()
        if action == BLACK_CARD_ACTION:
            card = self.deck.pick_next('black')
        elif action == SIEGE_ACTION:
            self.gameboard.sieges += 1
        elif action == LOSE_LIFE_ACTION:
            knight.life -= 1

    def heroic_action_phase(self, knight):
        action = knight.choose_heroic_action()
        if action == MOVE_ACTION:
            knight.choose_new_location(self.gameboard.current_positions)
        elif action == CURRENT_QUEST_ACTION:
            pass
        elif action == SPECIAL_CARD_ACTION:
            pass
        elif action == HEAL_ACTION:
            pass



if __name__ == '__main__':
    gameboard = Gameboard()
    testgame = Game(gameboard, 4)
    testgame.play()
