from Game import Game

def main():
    numOfPlayers = int(input('Enter number of players : '))
    game = Game(2 if numOfPlayers<2 else numOfPlayers)
    game.start()

main()