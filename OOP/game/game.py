from player import Player
from revolver import Revolver

def play_game(players):
    game_over = False
    while not game_over:
        for player in players:
            game_over = player.shoot()
            if game_over:
                break

def create_player():
    revolver = Revolver()
    players = [
        Player('Иван', revolver),
        Player('Атай', revolver),
        Player('Данияр', revolver)
    ]
    return players