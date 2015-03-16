import random

ROUNDTABLE = "round_table"
EXCALIBUR = "excalibur"
HOLYGRAIL = "holy_grail"
LANCELOT = "lancelot"


class Gameboard:

    def __init__(self):
        self.round_table = RoundTable()
        self.sieges = 0
        self.quests = [QuestFactory.Excalibur(),
                       QuestFactory.HolyGrail(),
                       QuestFactory.Lancelot()]

    def has_black_sword_majority(self):
        return self.round_table.black_swords >= 7

    def move(self, knight, position):
        knight.current_position = position


class RoundTable:

    def __init__(self):
        self.black_swords = 0
        self.white_swords = 0

    def is_full(self):
        assert(self.black_swords + self.white_swords < 13)
        return self.black_swords + self.white_swords == 12


class QuestFactory:

    @staticmethod
    def Excalibur():
        return DoubleSidedQuest(EXCALIBUR)

    @staticmethod
    def HolyGrail():
        return DoubleSidedQuest(HOLYGRAIL)

    @staticmethod
    def Lancelot():
        return DoubleSidedQuest(LANCELOT)


class Quest:

    def __init__(self, name):
        self.name = name
        self.white_card_spots = None
        self.black_card_spots = None
        self.is_solo = False
        self.spoils = None
        self.punishment = None


class DoubleSidedQuest(Quest):

    def __init__(self, name):
        Quest.__init__(self, name)
        self.initial_side = True


class Deck:

    def __init__(self):
        self.white_cards = CardFactory.WhiteCards()
        self.black_cards = CardFactory.BlackCards()
        self.shuffle_all()

    def shuffle_all(self):
        random.shuffle(self.black_cards)
        random.shuffle(self.white_cards)

    def pick_card_with(self, name, color):
        card = self.search_one_card_with(name, color)
        self.remove_card(card, color)
        return card

    def pick_next(self, color):
        if color == 'white':
            card = self.white_cards[0]
        else:
            card = self.remove_cards[0]
        self.remove_card(card, color)
        return card

    def remove_card(self, card, color):
        if color == 'white':
            index = self.white_cards.index(card)
            self.white_cards = self.white_cards[:index] + self.white_cards[index+1:]
        else:
            index = self.black_cards.index(card)
            self.black_cards = self.black_cards[:index] + self.black_cards[index+1:]

    def search_one_card_with(self, name, color):
        all_cards = self.search_all_cards_with(name, color)
        if all_cards:
            return all_cards[0]
        else:
            return []

    def search_all_cards_with(self, name, color):
        if color == 'white':
            return [card for card in self.white_cards if card.name == name]
        else:
            return [card for card in self.black_cards if card.name == name]


    def __str__(self):
        return '\n'.join(map(str, self.white_cards + self.black_cards))


class CardSpot:
    pass


class CardFactory:

    @staticmethod
    def WhiteCards():
        cards = []
        for _ in range(14):
            cards.append(Card('fight', 'white', 'standard'))
        for _ in range(12):
            cards.append(Card('fight', 'white', 'standard'))
        for _ in range(10):
            cards.append(Card('fight', 'white', 'standard'))
        for _ in range(8):
            cards.append(Card('fight', 'white', 'standard'))
        for _ in range(7):
            cards.append(Card('fight', 'white', 'standard'))
        for _ in range(18):
            cards.append(Card('grail', 'white', 'standard'))

        for _ in range(7):
            cards.append(Card('merlin', 'white', 'special'))
        cards.append(Card('piety', 'white', 'special'))
        cards.append(Card('fate', 'white', 'special'))
        cards.append(Card('heroism', 'white', 'special'))
        cards.append(Card('reinforcements', 'white', 'special'))
        cards.append(Card('messenger', 'white', 'special'))
        cards.append(Card('lady_of_the_lake', 'white', 'special'))
        cards.append(Card('convocation', 'white', 'special'))
        cards.append(Card('clairvoyance', 'white', 'special'))
        return cards

    @staticmethod
    def BlackCards():
        cards = []
        for _ in range(5):
            cards.append(Card('black_knight', 'black', 'standard'))
        for _ in range(3):
            cards.append(Card('black_knight', 'black', 'standard'))
        for _ in range(2):
            cards.append(Card('black_knight', 'black', 'standard'))
        cards.append(Card('black_knight', 'black', 'standard'))
        for _ in range(4):
            cards.append(Card('lancelot_dragon', 'black', 'standard'))
        for _ in range(3):
            cards.append(Card('lancelot_dragon', 'black', 'standard'))
        for _ in range(3):
            cards.append(Card('lancelot_dragon', 'black', 'standard'))
        cards.append(Card('lancelot_dragon', 'black', 'standard'))
        for _ in range(15):
            cards.append(Card('despair', 'black', 'standard'))
        for _ in range(4):
            cards.append(Card('mercenaries', 'black', 'standard'))
        for _ in range(4):
            cards.append(Card('picts', 'black', 'standard'))
        for _ in range(4):
            cards.append(Card('saxons', 'black', 'standard'))

        cards.append(Card('dark_forest', 'black', 'special'))
        cards.append(Card('desolation', 'black', 'special'))
        cards.append(Card('desolation', 'black', 'special'))
        cards.append(Card('vivien', 'black', 'special'))
        cards.append(Card('mists_of_avalon', 'black', 'special'))
        cards.append(Card('guineviere', 'black', 'special'))
        cards.append(Card('morgan1', 'black', 'special'))
        cards.append(Card('morgan2', 'black', 'special'))
        cards.append(Card('morgan3', 'black', 'special'))
        cards.append(Card('morgan4', 'black', 'special'))
        cards.append(Card('morgan5', 'black', 'special'))
        cards.append(Card('mordred', 'black', 'special'))
        return cards


class Card:

    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

    def __repr__(self):
        return self.name + "," + self.color + "," + self.type


class Knight:

    def __init__(self, name):
        self.name = name
        self.life = 4
        self.relic = None
        self.special_power = None
        self.current_position = None
        self.cards = []


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
    testgame = Game(gameboard, 0)
    assert(testgame.is_lost())
    testgame = Game(gameboard, 4)
    assert(testgame.is_lost() == False)
    testgame.gameboard.sieges = 12
    assert(testgame.is_lost())
    for k in testgame.knights:
        print k.name, k.current_position
    print testgame.deck
    testgame.start_game()
    print [x.cards for x in testgame.knights]