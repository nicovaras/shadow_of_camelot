class RoundTable:

    def __init__(self):
        self.black_swords = 0
        self.white_swords = 0

    def is_full(self):
        assert(self.black_swords + self.white_swords < 13)
        return self.black_swords + self.white_swords == 12