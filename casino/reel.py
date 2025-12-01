import random
from settings import SYMBOLS

class Reel:
    def spin(self):
        return random.choice(SYMBOLS)
    
