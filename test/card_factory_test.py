import card_factory
import unittest 
class TestCardFactory(unittest.TestCase):

    def test_card_factory(self):
        cf = card_factory.CardFactory()
        self.assertEquals(84, len(cf.WhiteCards()))
        self.assertEquals(76, len(cf.BlackCards()))

    def test_car_eq(self):
        cf = card_factory.CardFactory()
        fights = [card for card in cf.WhiteCards() if card.name == "fight"]
        merlins = [card for card in cf.WhiteCards() if card.name == "merlin"]
        for i in range(len(fights)-1):
            self.assertEquals(fights[i], fights[i+1])
        self.assertFalse(fights[0] == merlins[0])