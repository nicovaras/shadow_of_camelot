import random
from gameboard import Gameboard 
from knight import Knight
from constants import *





class CardSpot:
    pass









class SpecialPower:

    def __init__(self):
        pass


class SiegeEngine:
    pass


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
            self.progression_of_evil_phase()
            if self.is_ended():
                break
            
            self.heroic_action_phase()
            if self.is_ended():
                break

    def progression_of_evil_phase(self):
        ## TEST
        self.gameboard.round_table.white_swords += 1
        print self.gameboard.round_table.white_swords

    def heroic_action_phase(self):
        pass


class KnightFactory:

    @staticmethod
    def Arthur():
        knight = Knight("Arthur")
        return knight

    @staticmethod
    def Gawain():
        knight = Knight("Gawain")
        return knight

    @staticmethod
    def Galahad():
        knight = Knight("Galahad")
        return knight

    @staticmethod
    def Kay():
        knight = Knight("Kay")
        return knight

    @staticmethod
    def Palamedes():
        knight = Knight("Palamedes")
        return knight

    @staticmethod
    def Percival():
        knight = Knight("Percival")
        return knight

    @staticmethod
    def Tristan():
        knight = Knight("Tristan")
        return knight

if __name__ == '__main__':
    gameboard = Gameboard()
    # testgame = Game(gameboard, 0)
    # assert(testgame.is_lost())
    testgame = Game(gameboard, 4)
    # assert(testgame.is_lost() == False)
    # testgame.gameboard.sieges = 12
    # assert(testgame.is_lost())
    # for k in testgame.knights:
    #     print k.name, k.current_position
    # print testgame.deck
    testgame.play()
    # print [x.cards for x in testgame.knights]