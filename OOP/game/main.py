from game import play_game, create_player

if __name__ == '__main__':
    print("===Русская рулетка!===")
    players = create_player()
    play_game(players)
    print("===Игра окончена===")