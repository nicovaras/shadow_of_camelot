from constants import *

class QuestFactory:

    @staticmethod
    def Excalibur():
        return DoubleSidedQuest(EXCALIBUR)

    @staticmethod
    def HolyGrail():
        return DoubleSidedQuest(HOLYGRAIL)

    @staticmethod
    def Lancelot():
        return DoubleSidedQuest(LANCELOT)


class Quest:

    def __init__(self, name):
        self.name = name
        self.white_card_spots = None
        self.black_card_spots = None
        self.is_solo = False
        self.spoils = None
        self.punishment = None


class DoubleSidedQuest(Quest):

    def __init__(self, name):
        Quest.__init__(self, name)
        self.initial_side = True