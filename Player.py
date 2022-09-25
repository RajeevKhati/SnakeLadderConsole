class Player:
    def __init__(self, name):
        self.position = 0
        self.name = name
    
    def changePosition(self, diceNum):
        if self.position+diceNum > 100:
            print("You can't go beyond 100, wait for your turn.")
            return
        self.position = self.position + diceNum
    
    def setPosition(self, position):
        self.position = position
    
    def __str__(self) -> str:
        return f"Player {self.name} is at position {self.position}"