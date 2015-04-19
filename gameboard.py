from roundtable import RoundTable
from quest import QuestFactory

class Gameboard:

    def __init__(self):
        self.round_table = RoundTable()
        self.sieges = 0
        self.quests = [QuestFactory.Excalibur(),
                       QuestFactory.HolyGrail(),
                       QuestFactory.Lancelot()]
        self.current_positions = {}

    def has_black_sword_majority(self):
        return self.round_table.black_swords >= 7

    def move(self, knight, position):
        self.current_positions[knight] = position