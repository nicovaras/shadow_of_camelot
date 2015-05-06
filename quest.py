from constants import *

class QuestFactory:

    @staticmethod
    def Excalibur():
        return Quest(EXCALIBUR)

    @staticmethod
    def HolyGrail():
        return Quest(HOLYGRAIL)

    @staticmethod
    def Lancelot():
        quest = Quest(LANCELOT)
        quest.is_solo = True
        quest.other_side = QuestFactory.Dragon()
        return quest
    
    @staticmethod
    def Dragon():
        quest = Quest(DRAGON)
    
    @staticmethod
    def BlackKnight():
        quest = Quest(BLACK_KNIGHT)
        quest.is_solo = True
        return quest

    @staticmethod
    def Picts():
        return Quest(PICTS)

    @staticmethod
    def Saxons():
        return Quest(SAXONS)


class Quest:

    def __init__(self, name):
        self.name = name
        self.white_card_spots = None
        self.black_card_spots = None
        self.is_solo = False
        self.spoils = None
        self.punishment = None
        self.other_side = None