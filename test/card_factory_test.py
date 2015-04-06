import card_factory
import unittest 
class TestCardFactory(unittest.TestCase):

    def test_card_factory(self):
        cf = card_factory.CardFactory()
        self.assertEquals(84, len(cf.WhiteCards()))
        self.assertEquals(76, len(cf.BlackCards()))