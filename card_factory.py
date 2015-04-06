from card import Card

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
        for _ in range(15):
            cards.append(Card('excalibur', 'black', 'standard'))
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