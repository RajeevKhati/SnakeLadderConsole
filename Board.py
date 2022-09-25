from Dice import Dice

class Board:
    def __init__(self, snakes, ladders, players):
        self.snakes = snakes
        self.ladders = ladders
        self.players = players
        self.size = 100
        self.currentPlayerIdx = 0
        self.dice = Dice()
        self.numOfPlayers = len(players)
    
    def __str__(self) -> str:
        return f"Board snakes:{self.snakes}, ladders:{self.ladders}, players:{self.players}, size:{self.size}"

    def playChance(self):
        diceNum = self.dice.rollDice()
        currentPlayer = self.players[self.currentPlayerIdx]
        currentPlayer.changePosition(diceNum)
        bittenBySnake = False
        for snake in self.snakes:
            if snake.start == currentPlayer.position:
                bittenBySnake = True
                print(f'You got bitten by a snake at {snake.start}')
                currentPlayer.setPosition(snake.end)
        
        if not bittenBySnake:
            for ladder in self.ladders:
                if ladder.start == currentPlayer.position:
                    print(f'You got a ladder at {ladder.start}')
                    currentPlayer.setPosition(ladder.end)
        
        print("")
        print('Current Status:')
        self.displayAllPlayersPosition()
        print("")
        isWinner = currentPlayer.position == self.size
        self.currentPlayerIdx = (self.currentPlayerIdx+1) % self.numOfPlayers
        return isWinner


    def displayAllPlayersPosition(self):
        for player in self.players:
            print(player)

    def displayBoardInfo(self):
        print("")
        for snake in self.snakes:
            print(snake)
        print("")
        for ladder in self.ladders:
            print(ladder)
        print("")