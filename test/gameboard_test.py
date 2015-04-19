import gameboard
import unittest
import knight

class TestGameboard(unittest.TestCase):

    def test_move(self):
        k = knight.Knight("test")
        testboard = gameboard.Gameboard()
        self.assertTrue(testboard.current_positions == {})
        testboard.move(k, "test_position")
        self.assertTrue(testboard.current_positions[k] == "test_position")

