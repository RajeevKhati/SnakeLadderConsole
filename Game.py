import random
from Board import Board
from Ladder import Ladder
from Pair import Pair
from Player import Player
from Snake import Snake

class Game:
    def __init__(self, numOfPlayers):
        self.numOfPlayers = numOfPlayers
    
    def start(self):
       board = self.setupGameBoard()
       while True:
        currentPlayerName = board.players[board.currentPlayerIdx].name
        userInput = input(f'''It's {currentPlayerName}'s chance. Press enter to roll dice''')
        if(userInput=='q' or userInput=='Q'):
            break
        isWinner = board.playChance()
        if(isWinner):
            print(f"Player {currentPlayerName} won the Game.. Congratulations!!!")
            break 
    
    def setupGameBoard(self):
        players = self.getPlayers()
        gameBoard = None
        isFirstLoop = True
        while True:
            randomNum = self.getRandomNum()
            snakes = self.getSnakesConfig(randomNum) #array of Snake
            ladders = self.getLaddersConfig(randomNum) #array of Ladder
            gameBoard = Board(snakes, ladders, players)
            print("")
            print('Board Information:- ')
            gameBoard.displayBoardInfo()

            isChange = input(f'''Do you{" " if isFirstLoop else " still "}want to change current board configuration? Press 'y' and 'Enter' to change board. ''')
            if(isChange=='y' or isChange=='Y'):
                isFirstLoop = False
            else:
                break
        
        return gameBoard
    
    def getSnakesConfig(self,randomNum):
        snakeEndPoints = self.getSnakeEndPoints(randomNum)
        snakeConfig = []
        for key in snakeEndPoints.keys():
            snakeStart = key
            snakeEnd = snakeEndPoints[key]
            snakeConfig.append(self.getSnake(snakeStart, snakeEnd))
        return snakeConfig;
    
    def getLaddersConfig(self, randomNum):
        ladderEndPoints = self.getLadderEndPoints(randomNum)
        ladderConfig = []
        for key in ladderEndPoints.keys():
            ladderStart = key
            ladderEnd = ladderEndPoints[key]
            ladderConfig.append(self.getLadder(ladderStart, ladderEnd))
        return ladderConfig;
    
    def getPlayers(self):
        players = []
        for i in range(self.numOfPlayers):
            name = input(f"Enter name of player {i+1} : ")
            players.append(Player(name))
        return players
    
    def getSnakeEndPoints(self, num):
        arrOfSnakeEndPoints = [
            {32:10, 36:6, 48:26, 62:18, 88:24, 95:56, 97:78},
            {17:7, 62:19, 54:34, 64:60, 87:36, 93:73, 94:75, 98:79},
            {29:9, 38:15, 47:5, 53:33, 62:37, 86:54, 92:70, 97:25},
            {6:3, 51:13, 42:21, 56:36, 67:54, 83:62, 91:87, 96:66},
        ]
        return arrOfSnakeEndPoints[num];
    
    def getLadderEndPoints(self, num):
        arrOfLadderEndPoints = [
            {1:38, 4:14, 8:30, 28:76, 21:42, 50:67, 80:99, 71:92},
            {3:37, 5:15, 9:31, 28:84, 21:42, 51:67, 81:97, 72:91},
            {2:23, 8:34, 32:68, 41:79, 74:88, 82:100, 85:95 },
            {5:9, 15:25, 18:80, 44:86, 47:68, 63:78, 71:94, 81:98},
        ]
        return arrOfLadderEndPoints[num];
    
    def getRandomNum(self):
        #Must be equal to snake and ladder endpoints list
        return random.randint(0,3)
    
    def getSnake(self, start, end):
        pair = Pair(start, end)
        snake = Snake(pair)
        return snake
    
    def getLadder(self, start, end):
        pair = Pair(start, end)
        ladder = Ladder(pair)
        return ladder