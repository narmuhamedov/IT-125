import random
from exceptions import BangException

class Revolver:
    def __init__(self, chambers=6):
        self.chambers = chambers
        self.bullet_postion = random.randint(1, chambers)
        self.current_postion = 1

    def pull_trigger(self):
        if self.current_postion == self.bullet_postion:
            raise BangException('Бум! Выстрел')
        else:
            print('Щелк! Пусто')
        self.current_postion = (self.current_postion % self.chambers)+1
        