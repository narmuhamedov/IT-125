from reel import Reel

class SlotMachine:
    def __init__(self):
        self.reels = [Reel(), Reel(), Reel()]  # Используйте self.reels

    def spin(self):
        return [reel.spin() for reel in self.reels]
    
    def calculate_win(self, symbols, bet):
        if len(set(symbols)) == 1:
            return bet * 5
        if len(set(symbols)) == 2:
            return bet * 2
        return 0