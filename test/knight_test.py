import knight
import unittest 
import card_factory

class TestKnight(unittest.TestCase):

    def test_three_equals(self):
        cf = card_factory.CardFactory()
        k = knight.Knight("test")
        k.cards = cf.WhiteCards()
        names = [x.name for x in k.get_all_three_equal_cards()]
        for n in ['fight', 'grail', 'merlin']:
            self.assertIn(n, names)

    def test_discard_three(self):
        k = knight.Knight("test")
        cf = card_factory.CardFactory()
        k.cards = cf.WhiteCards()
        merlins = [x for x in k.cards if x.name == 'merlin']
        self.assertEquals(len(merlins), 7)
        k.choose_and_discard_three([merlins[0]])
        merlins = [x for x in k.cards if x.name == 'merlin']
        self.assertEquals(len(merlins), 4)
