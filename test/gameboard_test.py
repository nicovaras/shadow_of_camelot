import gameboard
import unittest
import knight

class TestGameboard(unittest.TestCase):

    def test_move(self):
        k = knight.Knight("test")
        self.assertTrue(k.current_position == None)
        testboard = gameboard.Gameboard()
        testboard.move(k, "test_position")
        self.assertTrue(k.current_position == "test_position")

