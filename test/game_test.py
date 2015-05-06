import deck
import unittest 
import shadow
from card import Card
from gameboard import Gameboard
from constants import *
from mock import MagicMock

class TestGame(unittest.TestCase):

    def setUp(self):
        self.g = shadow.Game(Gameboard(), 4)
    
    def test_init_knights(self):
        self.assertEquals(4, len(self.g.knights))
        knights = self.g.init_knights(7)
        self.assertEquals(7, len(knights))
        for k in knights:
            self.assertEquals(ROUNDTABLE, self.g.gameboard.current_positions[k])

    def test_is_lost(self):
        self.assertFalse(self.g.is_lost())
        
        self.g.gameboard.sieges = 12
        self.assertTrue(self.g.is_lost())
        
        self.g.gameboard.sieges = 0
        self.assertFalse(self.g.is_lost())

        self.g.gameboard.round_table.black_swords = 7
        self.assertTrue(self.g.is_lost())
        
        self.g.gameboard.round_table.black_swords = 0
        self.assertFalse(self.g.is_lost())

        for k in self.g.knights:
            k.life = 0
        self.assertTrue(self.g.is_lost())

    def test_all_died(self):
        self.assertFalse(self.g.is_lost())
        for k in self.g.knights:
            k.life = 0
        self.assertTrue(self.g.is_lost())

    def test_start_game(self):
        self.g.start_game()
        for k in self.g.knights:
            self.assertEquals(6, len(k.cards))
            self.assertIn('merlin', [x.name for x in k.cards])
            self.assertTrue(all([x.color == 'white' for x in k.cards]))

    def test_next_knight_turn(self):
        self.assertEquals(self.g.knights[0], self.g.next_knight_turn())
        self.assertEquals(self.g.knights[1], self.g.next_knight_turn())
        self.assertEquals(self.g.knights[2], self.g.next_knight_turn())
        self.assertEquals(self.g.knights[3], self.g.next_knight_turn())
        self.assertEquals(self.g.knights[0], self.g.next_knight_turn())

    def test_progression_evil(self):
        knight = self.g.knights[0]
        len_black = len(self.g.deck.black_cards)
        
        knight.choose_evil_action = MagicMock(return_value=BLACK_CARD_ACTION)
        self.g.progression_of_evil_phase(knight)
        self.assertEquals(len_black-1, len(self.g.deck.black_cards))

        knight.choose_evil_action = MagicMock(return_value=SIEGE_ACTION)
        self.g.progression_of_evil_phase(knight)
        self.assertEquals(1, self.g.gameboard.sieges)

        knight.choose_evil_action = MagicMock(return_value=LOSE_LIFE_ACTION)
        self.g.progression_of_evil_phase(knight)
        self.assertEquals(3, knight.life)
    
    def test_heroic_action(self):
        knight = self.g.knights[0]
        knight.cards = [Card('test', 'white', 'standard')] * 12      
        self.assertEquals(knight.life, 4)
        knight.choose_heroic_action = MagicMock(return_value=HEAL_ACTION)
        self.g.heroic_action_phase(knight)
        self.assertEquals(len(knight.cards), 9)
        self.assertEquals(knight.life, 5)
        self.g.heroic_action_phase(knight)
        self.assertEquals(len(knight.cards), 6)
        self.assertEquals(knight.life, 6)
        self.g.heroic_action_phase(knight)
        self.assertEquals(len(knight.cards), 3)
        self.assertEquals(knight.life, 6)
        self.g.heroic_action_phase(knight)
        self.assertEquals(len(knight.cards), 0)
        self.assertEquals(knight.life, 6)
        self.g.heroic_action_phase(knight)
        self.assertEquals(len(knight.cards), 0)
        self.assertEquals(knight.life, 6)
