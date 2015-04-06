import deck
import unittest 
class TestDeck(unittest.TestCase):

    def setUp(self):
        self.d = deck.Deck()
    
    def test_deck(self):
        self.assertTrue(self.d.white_cards)
        self.assertTrue(self.d.black_cards)

    def test_pick_one(self):
        self.assertEquals("merlin",
                          self.d.pick_card_with("merlin", "white").name)
        self.assertEquals(None,
                          self.d.pick_card_with("merlin", "black"))

    def test_pick_next(self):
        curr_len = len(self.d.white_cards)
        card = self.d.pick_next('white')
        self.assertEquals(curr_len - 1,len(self.d.white_cards))
        self.assertEquals('white', card.color)

    def test_remove(self):
        merlin_len = len([x for x in self.d.white_cards if x.name == 'merlin'])
        self.d.remove_card(self.d.search_one_card_with('merlin', 'white'), 'white')
        self.assertTrue(merlin_len - 1, 
                        len([x for x in self.d.white_cards if x.name == 'merlin']))

    def test_search_one(self):
        self.assertEquals('merlin', self.d.search_one_card_with('merlin','white').name)
        self.assertEquals(None, self.d.search_one_card_with('merlin','black'))

    def test_search_all(self):
        cards = self.d.search_all_cards_with('merlin','white')
        self.assertEquals(7, len(cards))
        self.assertTrue(all([x.name == 'merlin' for x in cards ] ))