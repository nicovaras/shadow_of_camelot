from card_factory import CardFactory
import random

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
        if card:
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
            return None

    def search_all_cards_with(self, name, color):
        if color == 'white':
            return [card for card in self.white_cards if card.name == name]
        else:
            return [card for card in self.black_cards if card.name == name]


    def __str__(self):
        return '\n'.join(map(str, self.white_cards + self.black_cards))