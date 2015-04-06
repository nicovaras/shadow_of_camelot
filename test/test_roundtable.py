import unittest
import roundtable

class TestRoundTable(unittest.TestCase):

    def test_full(self):
        test_table = roundtable.RoundTable()
        self.assertFalse(test_table.is_full())
        test_table.black_swords = 6
        test_table.white_swords = 5
        self.assertFalse(test_table.is_full())
        test_table.white_swords += 1
        self.assertTrue(test_table.is_full())
