from game import Game

if __name__ == "__main__":
    money = int(input('Введите кол-во денег: '))
    game = Game(money)
    game.run()