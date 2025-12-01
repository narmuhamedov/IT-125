import pygame
from slot_machine import SlotMachine
from logger import Logger
from settings import *

class Game:
    def __init__(self, money):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # Правильный порядок
        pygame.display.set_caption("CASINO GAME")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, FONT_SIZE)

        self.machine = SlotMachine()
        self.logger = Logger(LOG_FILE)
        self.money = money
        self.result = ["-", "-", "-"]
        self.message = "Нажмите на пробел чтобы начать игру!"

    def draw(self):
        self.screen.fill((20, 20, 20))
        x = 100

        for symbol in self.result:
            img = self.font.render(symbol, True, (255, 255, 255))
            self.screen.blit(img, (x, 150))
            x += 150
        
        msg = self.font.render(self.message, True, (0, 200, 0))
        self.screen.blit(msg, (20, 20))

        bal = self.font.render(f'Деньги: {self.money}', True, (200, 200, 0))
        self.screen.blit(bal, (20, 300))

        pygame.display.flip()
    
    def run(self):
        bet = 10
        running = True
        
        while running and self.money > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if self.money >= bet:
                        self.money -= bet
                        self.result = self.machine.spin()  
                        win = self.machine.calculate_win(self.result, bet)
                        self.money += win
                        self.message = f"ПОБЕДА: {win}" if win > 0 else "Вы проиграли!"
                        self.logger.write(f'{self.result} -> +{win} деньги = {self.money}')
                    else:
                        self.message = "Нет денег!"
            
            self.draw()
            self.clock.tick(FPS)
        
        self.logger.write("Игра окончена")
        pygame.quit()